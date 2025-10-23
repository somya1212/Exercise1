import pytest
mod = pytest.importorskip("eval.p04_candidate")
from eval.p04_candidate import factorial

def test_basic():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_larger():
    assert factorial(10) == 3628800
