
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create a dictionary to store the ASCII values of each character
    ascii_dict = {}
    # Iterate through the list of characters and calculate the ASCII value of each character
    for char in char_list:
        ascii_value = ord(char)
        ascii_dict[char] = ascii_value
    # Sort the dictionary by the ASCII values of the characters
    sorted_dict = sorted(ascii_dict.items(), key=lambda x: x[1])
    # Return the character with the 6th smallest ASCII value
    return sorted_dict[5][0]
