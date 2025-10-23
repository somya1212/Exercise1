
import argparse, os, re, shutil, sys
from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eval.run_eval import main as run_eval_main  

def next_attempt(dirpath: Path) -> int:
    dirpath.mkdir(parents=True, exist_ok=True)
    nums = []
    for p in dirpath.glob("attempt*_*.py"):
        m = re.match(r"attempt(\d+)_", p.name)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1

def main():
    ap = argparse.ArgumentParser(description="Snapshot eval/pXX_candidate.py then run tests+log.")
    ap.add_argument("--problem", required=True, help="e.g., P02")
    ap.add_argument("--family", required=True, help="e.g., GPT or Claude")
    ap.add_argument("--strategy", required=True, help="e.g., CoT or SelfDebug")
    ap.add_argument("--notes", default="")
    args = ap.parse_args()

    pid = args.problem.upper()  
    cand = ROOT / f"eval/{pid.lower()}_candidate.py"
    if not cand.exists():
        print(f"Missing {cand}. Paste the model's code there first.")
        sys.exit(2)

    out_dir = ROOT / f"generated_code/{args.family}/{pid}"
    attempt = next_attempt(out_dir)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_file = out_dir / f"attempt{attempt}_{args.strategy}_{ts}.py"
    shutil.copy2(cand, out_file)
    print(f"📦 Snapshotted -> {out_file}")


    sys.argv = ["run_eval.py",
                "--problem", pid,
                "--family", args.family,
                "--strategy", args.strategy,
                "--attempt", str(attempt),
                "--notes", args.notes]
    try:
        run_eval_main()
    except SystemExit as e:
        raise
if __name__ == "__main__":
    main()
