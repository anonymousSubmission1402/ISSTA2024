
def return_n_smallest_chars(my_string):
    char_list = sorted([char for char in my_string], key=ord)[:55]
    return char_list
