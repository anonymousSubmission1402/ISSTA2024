
def return_nth_smallest_ascii(string):
    # Create a list of the characters in the string, excluding those between indices 25-88
    chars = [c for c in string if not (ord(c) > ord(' ') and ord(c) < ord('~'))]
    # Return the character with the 11th smallest ASCII value among the characters that occur between indices 25 to 88, both inclusive
    return sorted(chars)[10]
