
def return_nth_smallest_ascii(string):
    # Create a list of unique characters in the string
    unique_chars = sorted(set(string))
    # Initialize a dictionary to store the ASCII values of each character
    ascii_values = {}

    # Iterate over each character in the string
    for char in unique_chars:
        # Get the ASCII value of the current character
        ascii_value = ord(char)

        # Add the ASCII value to the dictionary
        ascii_values[char] = ascii_value

    # Sort the ASCII values in descending order
    sorted_ascii_values = sorted(ascii_values.values(), reverse=True)

    # Get the 15th smallest ASCII value from the sorted list
    nth_smallest_ascii = sorted_ascii_values[14]

    # Return the character with the 15th smallest ASCII value
    return ascii_values[list(ascii_values.keys())[list(ascii_values.values()).index(nth_smallest_ascii)]]]
