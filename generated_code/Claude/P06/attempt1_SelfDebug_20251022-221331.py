def is_anagram(a: str, b: str) -> bool:
    clean_a = ''.join(c.lower() for c in a if c.isalnum())
    clean_b = ''.join(c.lower() for c in b if c.isalnum())
    return sorted(clean_a) == sorted(clean_b)