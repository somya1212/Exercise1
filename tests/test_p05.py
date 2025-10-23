import pytest
mod = pytest.importorskip("eval.p05_candidate")
from eval.p05_candidate import two_sum

def _check(nums, target, pair):
    i, j = pair
    assert 0 <= i < j < len(nums)
    assert nums[i] + nums[j] == target

def test_basic():
    nums = [2,7,11,15]
    target = 9
    _check(nums, target, two_sum(nums, target))

def test_with_duplicates():
    nums = [3,2,4]
    target = 6
    _check(nums, target, two_sum(nums, target))

def test_any_valid():
    nums = [1,3,3,4]
    target = 6
    _check(nums, target, two_sum(nums, target))
