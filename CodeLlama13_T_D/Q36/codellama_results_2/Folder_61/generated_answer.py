
def filter_chars(s):
    for i in range(3, 9):
        if s[i] > '*' and s[i] < 'E':
            s = s.replace(s[i], '')
    return s
