
def filter_chars(s):
    return ''.join([c for c in s if not (ord('1') < ord(c) < ord('J'))])
