
def filter_chars(s):
    # Create a new string with all characters removed that are between indices 225 and 381, both inclusive
    new_string = ""
    for i in range(len(s)):
        if (i < 225 or i > 381) or ('D' <= s[i] <= 'Y'):
            # Append the character to the new string if it is not between indices 225 and 381, both inclusive, or if it is between these indices and is greater than or equal to character 'D' and smaller than or equal to character 'Y'
            new_string += s[i]
    return new_string
