import pytest
from eval.p05_candidate import two_sum

def test_no_solution_returns_minus_one_tuple():
    nums = [1, 2, 3]
    assert two_sum(nums, target=100) == (-1, -1)

def test_pair_found_with_duplicates_earliest_indices():
    nums = [3, 3, 2]
    assert two_sum(nums, target=6) == (0, 1)

def test_pair_with_negative_and_positive_numbers():
    nums = [-1, 4, -3, 2]
    i, j = two_sum(nums, target=1)
    assert i != -1 and j != -1
    assert i != j
    assert nums[i] + nums[j] == 1


def test_pair_with_zeros_no_solution():
    nums = [0, 4, 3, 0]
    assert two_sum(nums, target=1) == (-1, -1)
