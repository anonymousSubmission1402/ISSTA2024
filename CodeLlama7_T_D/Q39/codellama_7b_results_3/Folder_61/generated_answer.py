
def return_n_greatest_chars(string):
    # Split the string into a list of characters
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 66 characters of the sorted list
    return sorted_list[:66]
