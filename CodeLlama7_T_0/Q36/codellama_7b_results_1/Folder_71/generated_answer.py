
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the current character is between the indices 82 and 89 (both exclusive)
        if 82 < ord(char) < 89:
            # And it is greater than '*' and smaller than '['
            if ord(char) > ord('*') and ord(char) < ord('['):
                # Skip this character in the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
