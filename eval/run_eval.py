
import argparse, csv, datetime, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

def run_pytest_for(test_file: str) -> bool:
    """
    Run pytest on a single test file and return True iff all tests passed.
    """
    try:
        import pytest
    except ImportError:
        print("pytest not installed. Run: pip install pytest")
        return False
    rc = pytest.main(["-q", test_file])
    return rc == 0

def append_log(problem_id: str, model_family: str, prompt_strategy: str, attempt_idx: int, passed: bool, notes: str=""):
    log_path = Path("results/log.csv")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not log_path.exists()

    with log_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp","problem_id","model_family","prompt_strategy","attempt_idx","pass_all_tests","notes"])
        writer.writerow([
            datetime.datetime.now().isoformat(timespec="seconds"),
            problem_id, model_family, prompt_strategy, attempt_idx,
            "1" if passed else "0",
            notes
        ])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", required=True, help="e.g., P01")
    parser.add_argument("--family", required=True, help="e.g., GPT or Claude")
    parser.add_argument("--strategy", required=True, help="e.g., CoT or SelfDebug")
    parser.add_argument("--attempt", type=int, default=1)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    pid = args.problem.upper()  # e.g., P01
    test_file = f"tests/test_{pid.lower()}.py"
    if not os.path.exists(test_file):
        print(f"Cannot find {test_file}")
        sys.exit(2)

    passed = run_pytest_for(test_file)
    append_log(pid, args.family, args.strategy, args.attempt, passed, args.notes)
    print(f"[{pid}] {'PASS' if passed else 'FAIL'} logged for {args.family} / {args.strategy} (attempt {args.attempt}).")
    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
