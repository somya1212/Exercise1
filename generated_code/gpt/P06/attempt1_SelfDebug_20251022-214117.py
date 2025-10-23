def is_anagram(a: str, b: str) -> bool:
    a_filtered = [ch.lower() for ch in a if ch.isalnum()]
    b_filtered = [ch.lower() for ch in b if ch.isalnum()]
    return sorted(a_filtered) == sorted(b_filtered)
