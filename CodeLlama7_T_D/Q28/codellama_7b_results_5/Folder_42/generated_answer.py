
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between indices 12 and 72
    indices = [i for i, c in enumerate(string) if 12 <= i <= 72]
    # Get the ASCII values of the characters at those indices
    ascii_values = [ord(c) for i, c in enumerate(string) if 12 <= i <= 72]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the character with the 13th smallest ASCII value
    return chr(sorted_ascii_values[12])
