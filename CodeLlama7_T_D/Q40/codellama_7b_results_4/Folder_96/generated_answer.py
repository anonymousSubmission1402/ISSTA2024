
def return_n_smallest_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the first 20 characters of the sorted list
    return sorted_list[:20]
