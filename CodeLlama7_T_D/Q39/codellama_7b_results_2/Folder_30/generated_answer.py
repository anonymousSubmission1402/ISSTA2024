
def return_n_greatest_chars(string, n=72):
    # Convert the string to a list of characters
    char_list = list(string)

    # Sort the list of characters by their ASCII values in descending order
    sorted_list = sorted(char_list, key=ord, reverse=True)

    # Return the first n elements of the sorted list
    return sorted_list[:n]
