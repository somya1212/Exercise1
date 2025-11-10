import pytest
from eval.p09_candidate import roman_to_int

@pytest.mark.parametrize(
    "s, expected",
    [
        ("XLII", 42),     # 40 + 2
        ("XCIX", 99),     # 90 + 9
        ("CDXLIV", 444),  # 400 + 40 + 4
        ("LVIII", 58),    # 50 + 5 + 3
        ("MCMXCIV", 1994) # 1000 + 900 + 90 + 4
    ],
)
def test_composite_subtractive_and_mixed_cases(s, expected):
    assert roman_to_int(s) == expected

def test_invalid_character_raises_keyerror():
    with pytest.raises(KeyError):
        roman_to_int("AZ")
