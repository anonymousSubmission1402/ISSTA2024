
def filter_chars(s):
    s = list(s)
    for i in range(48, 75):
        if s[i].isalnum() and s[i] > '6' and s[i] < '_':
            s.remove(s[i])
    return "".join(s)
