def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """Return indices (i, j) with i < j such that nums[i] + nums[j] == target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i