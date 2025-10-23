def is_anagram(a: str, b: str) -> bool:
    """Return True if a and b are anagrams, ignoring case, spaces, and punctuation."""
    from string import punctuation
    clean_a = ''.join(ch.lower() for ch in a if ch.isalnum())
    clean_b = ''.join(ch.lower() for ch in b if ch.isalnum())
    return sorted(clean_a) == sorted(clean_b)