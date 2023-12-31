
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate through each character in the list and check if it is between the indices 49 and 56 (both exclusive)
    for i, char in enumerate(char_list):
        if 49 < ord(char) < 57:
            # If the character is between the indices 49 and 56 (both exclusive), remove all occurrences of that character within the string while keeping the order of all characters in the string intact.
            char_list = char_list[:i] + char_list[i+1:]
    # Join the list of characters into a single string and return it
    return "".join(char_list)
