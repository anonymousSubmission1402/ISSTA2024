
def filter_chars(s):
    s = list(s)
    for i in range(82, 93):
        c = chr(i)
        if '!' < c < '*':
            s = [x for x in s if x != c]
    return "".join(s)
