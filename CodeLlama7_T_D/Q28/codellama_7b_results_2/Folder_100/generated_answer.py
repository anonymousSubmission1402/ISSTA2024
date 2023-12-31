
def return_nth_smallest_ascii(string):
    # Get the characters that occur between indices 5 and 47
    char_list = string[5:48]
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 13th smallest ASCII value
    return sorted_list[12]
