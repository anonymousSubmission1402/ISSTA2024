
def return_n_smallest_chars(my_string):
    char_list = []
    for char in my_string:
        if char not in char_list:
            char_list.append(char)
    sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)
    return sorted_list[:49]
