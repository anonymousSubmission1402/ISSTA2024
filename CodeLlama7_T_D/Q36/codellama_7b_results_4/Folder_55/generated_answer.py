
def filter_chars(string):
    # Create a list of characters in the string
    char_list = list(string)
    # Iterate over the characters and remove any that are between the indices 3 and 5 (both exclusive)
    for i in range(len(char_list)):
        if 3 < i < 5:
            char_list[i] = ''
    # Join the list of characters back into a string
    filtered_string = ''.join(char_list)
    return filtered_string
