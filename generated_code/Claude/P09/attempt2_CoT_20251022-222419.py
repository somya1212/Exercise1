def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer with extended support.
    
    Handles:
    - Standard and non-standard forms (IIII, VV, LL, etc.)
    - Extended values beyond 3999
    - Case-insensitive input
    - Overlines for multiplication by 1000 (V̅ = 5000)
    - Ancient variants (ↁ = 5000, ↂ = 10000)
    
    Args:
        s: A Roman numeral string
        
    Returns:
        The integer value of the Roman numeral
    """
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'ↁ': 5000, 'ↂ': 10000
    }
    
    s = s.upper()
    total = 0
    i = 0
    
    while i < len(s):
        char = s[i]
        
        if char in ['\u0305', '\u0304', '\u0336']:
            i += 1
            continue
        
        curr_value = values.get(char, 0)
        
        if i + 1 < len(s) and s[i + 1] in ['\u0305', '\u0304', '\u0336']:
            curr_value *= 1000
            i += 2
            if i < len(s) and s[i] in ['\u0305', '\u0304', '\u0336']:
                i += 1
            if i < len(s):
                next_char = s[i]
                next_value = values.get(next_char, 0)
                if i + 1 < len(s) and s[i + 1] in ['\u0305', '\u0304', '\u0336']:
                    next_value *= 1000
                if curr_value < next_value:
                    total -= curr_value
                else:
                    total += curr_value
            else:
                total += curr_value
        else:
            if i + 1 < len(s):
                next_char = s[i + 1]
                if next_char not in ['\u0305', '\u0304', '\u0336']:
                    next_value = values.get(next_char, 0)
                    if i + 2 < len(s) and s[i + 2] in ['\u0305', '\u0304', '\u0336']:
                        next_value *= 1000
                    if curr_value < next_value:
                        total -= curr_value
                    else:
                        total += curr_value
                else:
                    total += curr_value
            else:
                total += curr_value
            i += 1
    
    return total