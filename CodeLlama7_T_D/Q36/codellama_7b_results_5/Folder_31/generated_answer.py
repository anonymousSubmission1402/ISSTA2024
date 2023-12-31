
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over each character in the original string
    for i in range(len(s)):
        # Check if the current character is between indices 14 and 75 (exclusive)
        if 13 < i < 76:
            # Check if the current character is greater than '9' and smaller than 'K'
            if s[i] > '9' and s[i] < 'K':
                # Skip this character in the new string
                continue

        # Add the current character to the new string
        new_str += s[i]

    # Return the filtered string
    return new_str
