
def return_n_smallest_chars(string):
    char_list = []
    for i in range(len(string)):
        if string[i] not in char_list:
            char_list.append(string[i])
    sorted_char_list = sorted(char_list)
    return sorted_char_list[:48]
