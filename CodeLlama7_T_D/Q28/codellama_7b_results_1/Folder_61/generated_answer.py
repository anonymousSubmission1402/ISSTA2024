
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Sort the list of characters by their ASCII values
    sorted_char_list = sorted(char_list, key=ord)
    # Return the character with the 10th smallest ASCII value among those that occur between indices 0 to 9, both inclusive.
    return sorted_char_list[9]
