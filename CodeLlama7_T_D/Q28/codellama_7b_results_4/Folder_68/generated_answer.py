
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the character with the 11th smallest ASCII value
    nth_smallest = sorted(char_list, key=ord)[10]
    return nth_smallest
