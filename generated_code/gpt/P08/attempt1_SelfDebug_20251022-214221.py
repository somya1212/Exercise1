def gcd(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return 0
    while b:
        a, b = b, a % b
    return abs(a)
