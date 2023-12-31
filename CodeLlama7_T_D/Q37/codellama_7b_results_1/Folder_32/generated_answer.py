
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate through the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 23 and 89, both inclusive
        if 23 <= i <= 89:
            # Check if the current character is greater than or equal to 'w' and smaller than or equal to '{')
            if char_list[i] >= 'w' and char_list[i] <= '}':
                # Remove all occurrences of the current character from the list
                char_list.remove(char_list[i])
    # Return the altered string
    return "".join(char_list)
