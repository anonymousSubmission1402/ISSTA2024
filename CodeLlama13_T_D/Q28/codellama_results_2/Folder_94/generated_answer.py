
def return_nth_smallest_ascii(s):
    s = s[6:59]
    chars = []
    for c in s:
        if c not in chars:
            chars.append(c)
    chars.sort()
    return chars[18]
