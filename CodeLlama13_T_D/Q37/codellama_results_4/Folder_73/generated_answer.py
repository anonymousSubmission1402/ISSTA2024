
def filter_chars(s):
    return ''.join([c for c in s if 22 <= ord(c) <= 85 and ord('7') <= ord(c) <= ord('e')])
