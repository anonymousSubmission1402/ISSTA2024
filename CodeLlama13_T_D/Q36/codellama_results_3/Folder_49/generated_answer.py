
def filter_chars(s):
    return ''.join([c for c in s if ord(c) not in range(46, 91) or c > 'D' and c < 'H'])
