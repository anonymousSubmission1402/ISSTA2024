
def return_nth_smallest_ascii(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Get the indices of all characters in the list that occur between indices 10 to 73, both inclusive
    indices = [i for i, x in enumerate(char_list) if 10 <= i <= 73]
    # Get the ASCII values of all characters at these indices
    ascii_values = [ord(char_list[i]) for i in indices]
    # Return the character with the 9th smallest ASCII value among those characters
    return chr(sorted(ascii_values)[8]))
