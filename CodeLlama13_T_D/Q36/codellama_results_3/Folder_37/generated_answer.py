
def filter_chars(s):
    chars = set()
    for i in range(44, 59):
        if s[i] > '/' and s[i] < '6':
            chars.add(s[i])
    for c in chars:
        s = s.replace(c, '')
    return s
