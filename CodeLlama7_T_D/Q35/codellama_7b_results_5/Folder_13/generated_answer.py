
def remove_repeat_chars(s):
    for i in range(46, 91):
        c = s[i]
        if c in s[46:i] and c not in s[i+1:91]:
            s = s.replace(c, "")
    return s
