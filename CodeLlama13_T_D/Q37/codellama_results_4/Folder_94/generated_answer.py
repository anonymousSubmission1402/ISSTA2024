
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 51 or ord(c) > 96 or (ord(c) >= 88 and ord(c) <= 112)])
