
def filter_chars(s):
    return ''.join([c for c in s if not (19 <= ord(c) <= 22 and ord(']') <= ord(c) <= ord('t'))])
