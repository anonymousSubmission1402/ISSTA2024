
def filter_chars(s):
    res = ""
    for i, c in enumerate(s):
        if i >= 38 and i <= 99:
            if "A" <= c <= "Q":
                continue
        res += c
    return res
