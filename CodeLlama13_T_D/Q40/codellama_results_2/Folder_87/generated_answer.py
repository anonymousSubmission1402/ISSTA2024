
def return_n_smallest_chars(string):
    char_list = sorted([char for char in string if char.isalpha()])
    n = 24 if len(char_list) > 24 else len(char_list)
    return char_list[:n]
