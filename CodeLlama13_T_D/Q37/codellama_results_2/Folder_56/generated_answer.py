
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 71 or (ord(c) >= 94 and ord(c) <= 122)])
