import re
def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z][^A-Z]*', s, flags=re.I) if ord(c) >= 47 and ord(c) <= 70)
