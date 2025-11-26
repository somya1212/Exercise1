# exercise3/spec_tests/test_p05_specguided.py
#
# Spec-guided tests for two_sum based on the formal assertions.
# They check index types, ordering, sum-to-target, and (-1, -1) behaviour.

from eval.p05_candidate import two_sum


def test_spec_guided_valid_pair_simple_unique():
    nums = [1, 2, 3]
    target = 5

    i, j = two_sum(nums, target)

    # There *is* a unique valid pair (1, 2), but the spec only requires
    # that we return some valid i < j with nums[i] + nums[j] == target.
    assert isinstance(i, int) and isinstance(j, int)
    assert 0 <= i < j < len(nums)
    assert nums[i] + nums[j] == target


def test_spec_guided_no_pair_returns_minus_one_pair():
    nums = [1, 2, 3]
    target = 100

    i, j = two_sum(nums, target)

    # No pair exists; must return (-1, -1)
    assert (i, j) == (-1, -1)
    # Ensure no mixed use of -1 like (-1, k) or (k, -1)
    assert (i == -1 and j == -1) or (i != -1 and j != -1)

    # And indeed, there is no valid pair in the input.
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            assert nums[a] + nums[b] != target


def test_spec_guided_very_short_lists():
    # Empty list
    nums_empty = []
    target = 0
    i_empty, j_empty = two_sum(nums_empty, target)
    assert (i_empty, j_empty) == (-1, -1)

    # Single-element list
    nums_single = [10]
    target_single = 10
    i_single, j_single = two_sum(nums_single, target_single)
    assert (i_single, j_single) == (-1, -1)

    # In both cases, no valid index pair exists
    assert len(nums_empty) < 2
    assert len(nums_single) < 2


def test_spec_guided_negatives_and_unique_pair():
    nums = [-3, 1, 4, 2]
    target = -1  # -3 + 2 = -1

    i, j = two_sum(nums, target)

    # Only one real pair exists in the data, but we just enforce the spec:
    assert isinstance(i, int) and isinstance(j, int)
    assert 0 <= i < j < len(nums)
    assert nums[i] + nums[j] == target


def test_spec_guided_zeros_and_unique_pair():
    nums = [0, 0, 5]
    target = 0

    i, j = two_sum(nums, target)

    # Any (i, j) with i < j and nums[i] + nums[j] == 0 is acceptable.
    assert isinstance(i, int) and isinstance(j, int)
    assert 0 <= i < j < len(nums)
    assert nums[i] + nums[j] == target


def test_spec_guided_duplicates_multiple_possible_pairs():
    nums = [2, 2, 2]
    target = 4  # Many valid pairs

    i, j = two_sum(nums, target)

    # Indices must form a valid ordered pair that sums to target.
    assert isinstance(i, int) and isinstance(j, int)
    assert 0 <= i < j < len(nums)
    assert i != -1 and j != -1
    assert nums[i] + nums[j] == target


def test_spec_guided_no_pair_with_negatives_and_positives():
    nums = [-5, -1, 2, 4]
    target = 10  # No combination sums to 10

    i, j = two_sum(nums, target)

    # Must signal absence with (-1, -1), not a mixed pair.
    assert (i, j) == (-1, -1)
    assert (i == -1 and j == -1) or (i != -1 and j != -1)

    # Double-check input really has no solution.
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            assert nums[a] + nums[b] != target
