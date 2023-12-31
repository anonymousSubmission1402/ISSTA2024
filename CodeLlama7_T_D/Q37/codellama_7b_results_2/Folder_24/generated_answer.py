
def filter_chars(my_string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Loop through each character in the input string
    for char in my_string:
        # Check if the current character is between indices 36 and 79, both inclusive
        if 36 <= my_string.index(char) <= 79:
            # Check if the current character is greater than or equal to '2' and smaller than or equal to 's'
            if char >= "2" and char <= "s":
                # Skip adding this character to the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
