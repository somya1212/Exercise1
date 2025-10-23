import pytest
mod = pytest.importorskip("eval.p07_candidate")
from eval.p07_candidate import unique_sorted

def test_basic():
    assert unique_sorted([3,1,3,2]) == [1,2,3]

def test_negatives():
    assert unique_sorted([0,-1,-1,5,2,5]) == [-1,0,2,5]

def test_empty():
    assert unique_sorted([]) == []
