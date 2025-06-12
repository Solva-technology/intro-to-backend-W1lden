def reverse_string(string: str) -> str:
    rev_str = ""
    for s in range(1, len(string) + 1):
        rev_str = rev_str + string[-s]
    return rev_str