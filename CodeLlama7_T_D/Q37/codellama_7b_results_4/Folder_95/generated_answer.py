
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Loop through each character in the given string
    for char in string:
        # If the current character is between indices 35 and 40, both inclusive, and is greater than or equal to character ')' and smaller than or equal to character 'l', then remove all occurrences of that character from the filtered string
        if (char >= "(") and (char <= "l") and ((char.lower()) in string[35:41])):
            # Remove all occurrences of the current character from the filtered string
            filtered_string = filtered_string.replace(char, "")

        # Otherwise, just append the current character to the filtered string
        else:
            filtered_string += char

    # Return the altered string
    return filtered_string
