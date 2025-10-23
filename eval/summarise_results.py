import pandas as pd

df = pd.read_csv("results/log.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["pass_all_tests"] = pd.to_numeric(df["pass_all_tests"], errors="coerce").fillna(0).astype(int)
first = (
    df.sort_values("timestamp")
      .groupby(["problem_id","model_family","prompt_strategy"], as_index=False)
      .first()
)

p1 = (
    first.groupby(["model_family","prompt_strategy"])["pass_all_tests"]
         .agg(count="size", num_pass="sum", pass_at_1="mean")
         .reset_index()
)
p1["pass_at_1"] = p1["pass_at_1"].round(3)

best = (
    df.groupby(["problem_id","model_family","prompt_strategy"])["pass_all_tests"]
      .max()  
      .reset_index(name="any_pass")
)

best_summary = (
    best.groupby(["model_family","prompt_strategy"])["any_pass"]
        .agg(count="size", num_pass="sum", best_rate="mean")
        .reset_index()
)
best_summary["best_rate"] = best_summary["best_rate"].round(3)

pivot = (
    best.pivot(index="problem_id",
               columns=["model_family","prompt_strategy"],
               values="any_pass")
        .fillna(0).astype(int)
        .sort_index()
)

print("\n=== pass@1 (first logged attempt only) ===")
print(p1.to_string(index=False))

print("\n=== best-of attempts (any pass across attempts) ===")
print(best_summary.to_string(index=False))

print("\n=== per-problem pass matrix (best-of) ===")
print(pivot)
