
def return_n_greatest_chars(string):
    char_list = sorted(list(set(string)), key=ord, reverse=True)[:20]
    return ''.join(char_list)
