
def remove_repeat_chars(s):
    chars = {}
    for i in range(20, 93):
        if s[i] in chars:
            del s[i]
        else:
            chars[s[i]] = True
    return s
