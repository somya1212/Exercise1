import pytest
mod = pytest.importorskip("eval.p02_candidate")
from eval.p02_candidate import is_palindrome

def test_simple_true():
    assert is_palindrome("racecar") is True

def test_phrase_true():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_false():
    assert is_palindrome("hello") is False

def test_mixed():
    assert is_palindrome("No 'x' in Nixon") is True
