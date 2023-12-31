
def return_n_smallest_chars(string):
    smallest_chars = []
    for char in string:
        if len(smallest_chars) < 27:
            smallest_chars.append(char)
    sorted_chars = sorted(smallest_chars, key=lambda x: ord(x), reverse=True)
    return sorted_chars
