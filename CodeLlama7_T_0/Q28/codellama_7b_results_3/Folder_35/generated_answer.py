
def return_nth_smallest_ascii(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Get the ASCII values of all characters in the list
    ascii_values = [ord(char) for char in char_list]
    # Find the 7th smallest ASCII value in the list
    seventh_smallest = sorted(ascii_values)[6]
    # Return the character with the 7th smallest ASCII value
    return chr(seventh_smallest)
