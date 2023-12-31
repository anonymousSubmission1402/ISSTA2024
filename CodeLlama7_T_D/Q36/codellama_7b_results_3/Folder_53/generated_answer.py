
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 90 and 97 (exclusive)
        if 90 < ord(char) < 97:
            # If the current character is between these indices, check if it is greater than 'j' and smaller than 'w'
            if char > 'j' and char < 'w':
                # If the current character is between these indices and is greater than 'j' and smaller than 'w', remove all occurrences of this character within the string while keeping the order of all characters intact.
                filtered_chars.append(char)
            else:
                # If the current character is not between these indices or is not greater than 'j' and smaller than 'w', add it to the list of filtered characters.
                filtered_chars.append(char)
    # Return the altered string with all occurrences of filtered characters removed while keeping the order of all characters intact.
    return "".join(filtered_chars)
