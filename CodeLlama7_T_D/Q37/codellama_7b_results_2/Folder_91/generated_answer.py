
def filter_chars(s):
    for i in range(7, 9):
        if s[i] >= 'B' and s[i] <= 'H':
            s = s[:i] + s[i+1:]
    return s
