
def remove_repeat_chars(s):
    seen = set()
    res = ""
    for i in range(355, 988):
        if s[i] not in seen:
            res += s[i]
            seen.add(s[i])
    return res
