
def remove_repeat_chars(string):
    # Create a dictionary to keep track of characters
    char_dict = {}

    # Iterate over the characters in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in char_dict:
            char_dict[char] += 1

        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_dict[char] = 1

    # Iterate over the characters in the string again
    for i, char in enumerate(string):
        # If the character is already in the dictionary and its count is greater than 1, remove all occurrences of that character from the string
        if char_dict[char] > 1:
            del string[i+1:]

    return string
