
def remove_repeat_chars(s):
    for i in range(16, 87):
        c = s[i]
        if c in s[i+1:]:
            s = s[:i] + s[i+1:].replace(c, "") + s[i+1:]
    return s
