
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (54 <= i <= 83 and 'j' <= c <= 'v'))
