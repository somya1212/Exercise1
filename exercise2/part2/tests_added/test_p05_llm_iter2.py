import pytest
from eval.p05_candidate import two_sum

def test_no_solution_all_negatives():
    assert two_sum([-5, -4, -3], target=100) == (-1, -1)

def test_no_solution_large_numbers():
    assert two_sum([10**6, 10**7, 10**8], target=-1) == (-1, -1)

def test_multiple_pairs_returns_first_by_index_order():
    nums = [1, 2, 4, 5]
    i, j = two_sum(nums, target=6)
    assert (i, j) == (1, 2)

def test_repeated_numbers_with_self_complement_zero():
    nums = [0, 0, 1]
    assert two_sum(nums, target=0) == (0, 1)

def test_empty_or_singleton_gracefully_returns_minus_one_minus_one():
    assert two_sum([], target=1) == (-1, -1)
    assert two_sum([7], target=7) == (-1, -1)
