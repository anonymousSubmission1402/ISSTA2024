
def return_n_smallest_chars(s):
    char_list = []
    for i in range(35):
        temp_char = sorted(s, key=lambda x: ord(x))[i]
        char_list.append(temp_char)
    return char_list
