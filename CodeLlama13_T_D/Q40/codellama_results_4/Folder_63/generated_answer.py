
def return_n_smallest_chars(string):
    chars = sorted(list(set(string)), key=lambda x: ord(x))[:44]
    return chars
