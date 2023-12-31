
def return_nth_smallest_ascii(string):
    # Create a dictionary to keep track of the ASCII values
    ascii_values = {}

    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, skip it
        if char in ascii_values:
            continue

        # Add the character and its ASCII value to the dictionary
        ascii_values[char] = ord(char)

    # Sort the dictionary by key (character)
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[0])

    # Return the character with the 12th smallest ASCII value
    return sorted_ascii_values[12][0]
