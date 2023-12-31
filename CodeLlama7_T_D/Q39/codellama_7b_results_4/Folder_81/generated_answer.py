 def return_n_greatest_chars(s):
    # convert string to a list of characters
    char_list = list(s)
    # sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # return the top 64 characters from the sorted list
    return char_list[:64]
