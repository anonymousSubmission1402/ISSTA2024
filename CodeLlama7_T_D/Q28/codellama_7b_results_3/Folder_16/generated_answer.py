
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 18 and 45
    chars = string[18:46]
    # Initialize a list to store the ASCII values of the characters
    ascii_values = []

    # Iterate over the characters and add their ASCII values to the list
    for char in chars:
        ascii_values.append(ord(char))

    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)

    # Return the 7th smallest ASCII value
    return sorted_ascii_values[6]
