
def return_n_smallest_chars(s):
    char_list = sorted([c for c in s])
    return char_list[:2]
