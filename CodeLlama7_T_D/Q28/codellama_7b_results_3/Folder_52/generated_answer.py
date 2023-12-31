
def return_nth_smallest_ascii(string):
    # Create a list of unique characters in the string
    unique_chars = set(string)
    # Initialize a dictionary to store the ASCII values of each character
    ascii_values = {}
    # Iterate over each character in the string and store its ASCII value in the dictionary
    for char in string:
        if char not in ascii_values:
            ascii_values[char] = ord(char)
    # Sort the dictionary by value in ascending order
    sorted_values = sorted(ascii_values.items(), key=lambda x: x[1])
    # Return the character with the 15th smallest ASCII value
    return sorted_values[14][0]
