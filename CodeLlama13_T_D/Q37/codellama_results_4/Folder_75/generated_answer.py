
def filter_chars(s):
    return "".join([c for c in s if 34 <= ord(c) <= 67 and 'W' <= c <= 'x'])
