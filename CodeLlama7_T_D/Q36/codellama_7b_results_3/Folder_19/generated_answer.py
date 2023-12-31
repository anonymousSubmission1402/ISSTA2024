
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate over each character in the given string
    for char in string:
        # If the current character is between the indices 77 and 87 (both exclusive)
        if 76 < ord(char) < 88:
            # And it is greater than character ';' and smaller than character 'r', then remove all occurrences of that character within the string while keeping the order of all characters in the string intact.
            filtered_chars += [char for char in string if ord(char) != 77 and ord(char) != 87]
    # Return the altered string
    return "".join(filtered_chars)
