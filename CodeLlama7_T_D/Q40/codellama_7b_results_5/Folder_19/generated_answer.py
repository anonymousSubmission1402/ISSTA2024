
def return_n_smallest_chars(string):
    smallest_chars = []
    for char in string:
        if len(smallest_chars) < 58:
            smallest_chars.append(char)
    return sorted(smallest_chars)
