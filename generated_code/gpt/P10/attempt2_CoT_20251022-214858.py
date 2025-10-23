def longest_common_prefix(strs: list[str]) -> str:
    """Return the longest common prefix among all strings in the list."""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix