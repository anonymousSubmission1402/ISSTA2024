
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 54 or ord(c) > 38])
