def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b using Euclid's algorithm."""
    if a == 0 and b == 0:
        return 0
    while b:
        a, b = b, a % b
    return abs(a)