# exercise3/spec_tests/test_p09_specguided.py
#
# Spec-guided tests for roman_to_int based on the refined assertions.
# They check positivity, additive vs subtractive behaviour, and relationships
# between the numeral's symbol values and the computed result.

from eval.p09_candidate import roman_to_int


roman_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def _values(s: str) -> list[int]:
    return [roman_map[c] for c in s]


def test_spec_guided_single_symbols_match_value():
    """Spec 1 + 3: single-symbol numeral equals its symbol value, positive int."""
    for sym, val in roman_map.items():
        result = roman_to_int(sym)
        vals = _values(sym)

        assert isinstance(result, int)
        assert result > 0
        # single-symbol: result must equal the symbol's value
        assert len(sym) == 1
        assert result == vals[0] == val


def test_spec_guided_pure_additive_non_increasing():
    """
    Spec 2 + 4 + 6:
    If all values are non-increasing, numeral is additive-only and result
    equals the sum of symbol values.
    """
    for s in ["VIII", "LXIII", "MMVIII"]:
        vals = _values(s)
        result = roman_to_int(s)
        total_additive = sum(vals)

        # Non-increasing values = pure additive
        assert all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1))

        assert isinstance(result, int)
        assert result > 0
        # subtractive never larger than additive
        assert result <= total_additive
        # for fully additive numerals, result == additive sum
        assert result == total_additive


def test_spec_guided_simple_subtractive_pairs():
    """
    Spec 2 + 5 + 7:
    For two-character numerals with smaller before larger, result is
    (larger - smaller) and strictly less than the additive sum.
    """
    for s in ["IV", "IX", "XL", "XC", "CD", "CM"]:
        vals = _values(s)
        result = roman_to_int(s)
        total_additive = sum(vals)

        assert len(vals) == 2
        assert vals[0] < vals[1]  # subtractive pair

        # Two-symbol subtractive case: difference
        assert result == vals[1] - vals[0]

        # Result is positive and never exceeds additive sum
        assert isinstance(result, int)
        assert result > 0
        assert result <= total_additive
        # because there *is* a subtractive pair, result is strictly less
        assert result < total_additive


def test_spec_guided_mixed_subtractive_and_additive_compound_numerals():
    """
    Specs 1, 2, 6, 7 applied to longer numerals:
    - If any subtractive pair exists, result < total additive sum.
    - Still must give the mathematically correct integer.
    """
    samples = {
        "XLII": 42,      # 40 + 2
        "XCIX": 99,      # 90 + 9
        "CDXLIV": 444,   # 400 + 40 + 4
        "MCMXCIV": 1994  # 1000 + 900 + 90 + 4
    }

    for s, expected in samples.items():
        vals = _values(s)
        result = roman_to_int(s)
        total_additive = sum(vals)

        assert isinstance(result, int)
        assert result > 0

        # There is at least one subtractive pair in these numerals
        has_subtractive = any(
            vals[i] < vals[i + 1] for i in range(len(vals) - 1)
        )
        assert has_subtractive

        # With subtractive notation, result is strictly below additive sum
        assert result < total_additive

        # The combination of additive + subtractive rules yields this value
        assert result == expected


def test_spec_guided_mixed_but_pure_additive_example():
    """
    Sanity check: a longer numeral that is still purely additive
    (no subtractive pair) must match the additive sum exactly.
    """
    s = "MDCLXVI"  # 1000 + 500 + 100 + 50 + 10 + 5 + 1 = 1666
    vals = _values(s)
    result = roman_to_int(s)
    total_additive = sum(vals)

    assert all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1))
    assert isinstance(result, int)
    assert result > 0
    assert result == total_additive == 1666
