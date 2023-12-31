
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 25 and 64
    characters = string[25:64]
    # Create a list of the ASCII values of the characters
    ascii_values = [ord(c) for c in characters]
    # Sort the list in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 6th smallest ASCII value
    return sorted_ascii_values[5]
