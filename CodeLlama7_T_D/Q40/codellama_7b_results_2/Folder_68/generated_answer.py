
def return_n_smallest_chars(string, n=89):
    # Convert string to a list of characters
    char_list = list(string)
    # Sort the list in descending order based on ASCII value
    sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)
    # Return the first n elements of the sorted list
    return sorted_list[:n]
