def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer using standard subtractive rules.
    
    Args:
        s: A valid Roman numeral string (I, V, X, L, C, D, M)
        
    Returns:
        The integer value of the Roman numeral
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(s):
        curr = values[char]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total