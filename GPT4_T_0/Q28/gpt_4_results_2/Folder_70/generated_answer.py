
def return_nth_smallest_ascii(s):
    s = s[28:55]
    s = sorted(s, key=ord)
    return s[13]
