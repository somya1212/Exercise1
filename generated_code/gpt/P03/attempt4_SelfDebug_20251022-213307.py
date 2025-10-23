def is_palindrome(s: str) -> bool:
    """
    Returns the n-th Fibonacci number where F0 = 0 and F1 = 1.
    Interprets the input string s as an integer n (n >= 0).
    """
    n = int(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b