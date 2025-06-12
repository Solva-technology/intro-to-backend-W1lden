def reverse_string(string: str) -> str:
    reverted_string = list(string)
    reverted_string.reverse()
    return "".join(reverted_string)