
def return_n_greatest_chars(string):
    char_list = list(set(string))
    sorted_list = sorted(char_list, key=ord)
    return sorted_list[-47:]
