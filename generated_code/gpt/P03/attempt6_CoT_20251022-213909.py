def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number with F0=0 and F1=1 for n >= 0."""
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
