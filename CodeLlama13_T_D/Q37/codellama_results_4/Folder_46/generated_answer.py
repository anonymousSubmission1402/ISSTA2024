
def filter_chars(s):
    for i in range(11, 72+1):
        if s[i].isalpha() and 'i' <= s[i] <= 'v':
            s = s.replace(s[i], '')
    return s
