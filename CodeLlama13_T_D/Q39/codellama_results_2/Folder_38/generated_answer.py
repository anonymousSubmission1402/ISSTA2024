
def return_n_greatest_chars(s):
    n = 45
    chars = sorted(set(s), key=ord)
    return ''.join(chars[-n:])
