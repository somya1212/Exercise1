import pytest
mod = pytest.importorskip("eval.p03_candidate")
from eval.p03_candidate import fibonacci

def test_small():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13

def test_larger():
    assert fibonacci(20) == 6765
