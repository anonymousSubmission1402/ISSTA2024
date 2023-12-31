
def return_n_smallest_chars(my_string):
    # Create a list of characters from the input string
    char_list = list(my_string)
    # Sort the list in ascending order based on ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the first 82 characters of the sorted list
    return sorted_list[:82]
