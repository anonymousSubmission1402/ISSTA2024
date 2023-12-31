
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for c in s:
        # If the current character is not between 4 and 8 (inclusive), then append it to the filtered string
        if not (4 <= ord(c) <= 8):
            filtered += c

    # Return the filtered string
    return filtered
