
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over each character in the list and check if it is between indices 603 and 759, both inclusive
    for i in range(len(char_list)):
        # Check if the current character is between the specified indices
        if (i >= 603) and (i <= 759):
            # Check if the current character is greater than or equal to 'Q' and smaller than or equal to 'h'
            if (char_list[i] >= 'Q') and (char_list[i] <= 'h'):
                # Remove all occurrences of the current character from the string
                char_list = [c for c in char_list if c != char_list[i]]

    # Join the list of characters back into a string and return it
    return "".join(char_list)
