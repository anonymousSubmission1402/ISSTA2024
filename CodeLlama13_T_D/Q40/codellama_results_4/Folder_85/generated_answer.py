
def return_n_smallest_chars(string):
    chars = sorted(string, key=ord)[:85]
    return chars
