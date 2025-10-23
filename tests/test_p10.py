import pytest
mod = pytest.importorskip("eval.p10_candidate")
from eval.p10_candidate import longest_common_prefix

def test_basic():
    assert longest_common_prefix(["flower","flow","flight"]) == "fl"

def test_none():
    assert longest_common_prefix(["dog","racecar","car"]) == ""

def test_empty_list():
    assert longest_common_prefix([]) == ""
