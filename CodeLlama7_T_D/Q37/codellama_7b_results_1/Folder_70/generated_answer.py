 def filter_chars(s):
    # Create a set of all characters in the given string
    char_set = set(s)
    # Iterate over each character in the given string, checking if it is between indices 515 and 538, both inclusive
    for i, c in enumerate(s):
        # Check if the current character is greater than or equal to '+' and smaller than or equal to '}'
        if c in char_set and (i >= 515 and i <= 538):
            # Remove all occurrences of the current character from the string
            s = s.replace(c, "")
    return s
