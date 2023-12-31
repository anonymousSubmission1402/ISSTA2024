
def return_n_greatest_chars(input_string):
    # convert the input string to a list of characters
    char_list = list(input_string)
    # sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # return the top 54 characters from the sorted list
    return sorted_list[:54]
