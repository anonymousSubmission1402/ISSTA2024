
def remove_repeat_chars(s):
    for i in range(10, 28):
        if s[i - 1] == s[i]:
            s = s[:i - 1] + s[i:]
    return s
