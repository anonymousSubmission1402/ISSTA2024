
def return_n_smallest_chars(s):
    char_list = []
    for c in s:
        if c not in char_list:
            char_list.append(c)
    
    sorted_char_list = sorted(char_list, key=ord)
    return sorted_char_list[:79]
