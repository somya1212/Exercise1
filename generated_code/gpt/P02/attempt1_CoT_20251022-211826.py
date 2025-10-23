def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, considering only alphanumeric characters and ignoring case."""
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

