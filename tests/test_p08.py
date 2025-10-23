import pytest
mod = pytest.importorskip("eval.p08_candidate")
from eval.p08_candidate import gcd

def test_basic():
    assert gcd(54, 24) == 6
    assert gcd(24, 54) == 6

def test_with_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0
