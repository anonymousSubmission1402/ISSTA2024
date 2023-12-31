
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)

    # Calculate the ASCII value of each character and store it in a dictionary
    ascii_dict = {}
    for char in char_list:
        ascii_value = ord(char)
        ascii_dict[char] = ascii_value

    # Sort the dictionary by ASCII value
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1])

    # Return the character with the 7th smallest ASCII value
    return sorted_ascii_dict[6][0]
