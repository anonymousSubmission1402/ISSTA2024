
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 78 and ord(c) > 64])
