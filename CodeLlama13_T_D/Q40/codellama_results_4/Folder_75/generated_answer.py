
def return_n_smallest_chars(s):
    return sorted([x for x in set(s)], key=ord)[:2]
