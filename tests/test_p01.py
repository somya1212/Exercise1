import pytest
mod = pytest.importorskip("eval.p01_candidate")
from eval.p01_candidate import reverse_string

def test_basic():
    assert reverse_string("abc") == "cba"

def test_empty():
    assert reverse_string("") == ""

def test_unicode():
    assert reverse_string("नमस्ते") == "ेत्समन"
