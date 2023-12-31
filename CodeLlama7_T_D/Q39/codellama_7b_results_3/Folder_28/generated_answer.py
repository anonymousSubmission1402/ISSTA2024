
def return_n_greatest_chars(my_string):
    # Convert the string to a list of characters
    char_list = list(my_string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 3 characters with the greatest ASCII values
    return sorted_list[:3]
