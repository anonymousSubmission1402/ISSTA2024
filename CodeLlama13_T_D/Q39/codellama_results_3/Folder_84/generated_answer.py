
def return_n_greatest_chars(my_string):
    return sorted([char for char in my_string], key=ord)[:10]
