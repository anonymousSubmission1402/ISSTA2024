
def filter_chars(my_string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in my_string:
        # Check if the current character is between indices 1 and 5, both inclusive
        if 1 <= my_string.index(char) <= 5:
            # Check if the current character is greater than or equal to '$' and smaller than or equal to ';'
            if char >= '$' and char <= ';':
                # Skip adding this character to the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the altered string
    return filtered_string
