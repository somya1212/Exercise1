def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}
    for i, x in enumerate(nums):
        comp = target - x
        if comp in seen:
            return (seen[comp], i)
        seen[x] = i
    raise ValueError("No valid pair found")

