
def remove_repeat_chars(s):
    s = list(s)
    for i in range(10, 76):
        if s[i] in s[i+1:]:
            while s[i] in s[i+1:]:
                s.remove(s[i])
    return ''.join(s)
