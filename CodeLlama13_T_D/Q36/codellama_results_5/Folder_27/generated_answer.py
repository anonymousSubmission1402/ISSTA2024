
def filter_chars(s):
    for i in range(48, 75):
        if s[i].isalpha() and ord(s[i]) > 6 and ord(s[i]) < 95:
            s = s.replace(s[i], '')
    return s
