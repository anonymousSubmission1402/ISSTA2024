
def return_nth_smallest_ascii(string):
    # Create a list of the characters in the string
    char_list = list(string)
    # Get the ASCII values of all the characters in the list
    ascii_values = [ord(char) for char in char_list]
    # Find the 5th smallest ASCII value in the list
    fifth_smallest = sorted(ascii_values)[4]
    # Return the character with the 5th smallest ASCII value
    return chr(fifth_smallest)
