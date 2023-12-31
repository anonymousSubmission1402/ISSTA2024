
def remove_repeat_chars(s):
    # Initialize a list to store the characters of the input string
    char_list = []

    # Iterate over each character in the input string
    for char in s:

        # If the current character is not already in the list of characters, add it to the list
        if char not in char_list:
            char_list.append(char)

    # Initialize a new string to store the altered version of the input string
    altered_string = ""

    # Iterate over each character in the list of characters
    for char in char_list:

        # If the current character is not in the range of 200 and 202, add it to the altered string
        if char not in range(200, 203):
            altered_string += char

    return altered_string
