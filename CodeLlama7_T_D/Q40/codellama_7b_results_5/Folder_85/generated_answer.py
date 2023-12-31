
def return_n_smallest_chars(string):
    # create a list of characters from the input string
    char_list = list(string)
    # sort the list in descending order based on the ASCII value of each character
    sorted_char_list = sorted(char_list, key=lambda x: ord(x), reverse=True)
    # return the top 85 characters from the sorted list
    return sorted_char_list[:85]
