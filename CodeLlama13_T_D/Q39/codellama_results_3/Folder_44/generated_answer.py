
def return_n_greatest_chars(string):
    char_list = list(set(string))
    sorted_char_list = sorted(char_list, key=ord)
    return sorted_char_list[-73:]
