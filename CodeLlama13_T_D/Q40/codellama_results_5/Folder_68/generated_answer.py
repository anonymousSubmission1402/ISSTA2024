
def return_n_smallest_chars(s):
    chars = sorted(set(s), key=ord)
    return chars[:89]
