
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_dict = {}
    for char in string:
        if char not in ascii_dict:
            ascii_dict[char] = ord(char)
    # Sort the dictionary by value

    sorted_dict = {key: val for key, val in sorted(ascii_dict.items(), key=lambda item: item[1])}
    # Return the 6th smallest ASCII value

    return sorted_dict[6]
