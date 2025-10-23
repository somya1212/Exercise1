import pytest
mod = pytest.importorskip("eval.p09_candidate")
from eval.p09_candidate import roman_to_int

def test_examples():
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
