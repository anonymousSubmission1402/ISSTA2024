
def return_n_smallest_chars(string):
    sorted_list = sorted(set(string), key=ord)[:90]
    return sorted_list[::-1]
