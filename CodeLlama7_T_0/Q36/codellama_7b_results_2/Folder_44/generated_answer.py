
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 18 and 64 (both exclusive)
        if 18 < ord(char) < 64:
            # Check if the current character is greater than '3' and smaller than 'B'
            if char > '3' and char < 'B':
                # Skip this character since it needs to be filtered out
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
