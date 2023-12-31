
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Get the ASCII values of all characters in the list
    ascii_values = [ord(char) for char in char_list]
    # Find the 6th smallest ASCII value
    sixth_smallest = sorted(ascii_values)[5]
    # Return the character with the 6th smallest ASCII value
    return chr(sixth_smallest)
