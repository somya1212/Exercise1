import pytest
mod = pytest.importorskip("eval.p06_candidate")
from eval.p06_candidate import is_anagram

def test_true():
    assert is_anagram("Listen", "Silent!") is True

def test_spaces_punct_case():
    assert is_anagram("Dormitory", "Dirty room!!") is True

def test_false():
    assert is_anagram("apple", "pale") is False
