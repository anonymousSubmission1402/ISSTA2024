
def return_nth_smallest_ascii(string):
    # Create a list of characters in the string
    char_list = list(string)
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the 10th smallest ASCII value among the sorted list of characters
    return sorted_list[9]
