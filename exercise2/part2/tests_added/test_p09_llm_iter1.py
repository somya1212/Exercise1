import pytest
from eval.p09_candidate import roman_to_int

@pytest.mark.parametrize(
    "s, expected",
    [
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ],
)
def test_basic_numerals_and_repetitions(s, expected):
    assert roman_to_int(s) == expected

@pytest.mark.parametrize(
    "s, expected",
    [
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
    ],
)
def test_subtractive_pairs(s, expected):
    assert roman_to_int(s) == expected
