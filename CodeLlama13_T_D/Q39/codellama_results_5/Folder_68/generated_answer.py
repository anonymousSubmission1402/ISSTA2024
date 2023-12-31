
def return_n_greatest_chars(string):
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = ord(char)
    sorted_char_list = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)[:89]
    return [c for c, _ in sorted_char_list]
