
def filter_chars(s):
    s = list(s)
    for i in range(58, 81):
        if s[i].isalpha() and s[i] > "5" and s[i] < ">":
            s.remove(s[i])
    return ''.join(s)
