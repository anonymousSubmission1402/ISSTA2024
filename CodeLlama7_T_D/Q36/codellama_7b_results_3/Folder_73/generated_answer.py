
def filter_chars(string):
    # Create a new string with the filtered characters
    new_string = ""

    # Iterate over each character in the given string
    for char in string:

        # If the current character is between indices 66 and 90, and it is not equal to '#' or 'T', then remove all occurrences of this character from the new string while keeping the order of all characters intact.
        if (ord(char) > 65 and ord(char) < 84) and char != "#" and char != "T":
            # Replace all occurrences of the current character with an empty string in the new string
            new_string = new_string.replace(char, "")

        else:

            # If the current character is not between indices 66 and 90, or it is equal to '#' or 'T', then add this character to the new string while keeping the order of all characters intact.
            new_string += char

    return new_string
