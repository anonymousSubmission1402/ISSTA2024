
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over each character in the list
    for i, char in enumerate(char_list):
        # Check if the current character is between indices 1 and 7, both inclusive, and is greater than or equal to character 'L' and smaller than or equal to character 'a'
        if (i >= 1 and i <= 7) and (ord(char) >= ord('L') and ord(char) <= ord('a')):
            # Remove all occurrences of the current character from the list
            char_list = [c for c in char_list if c != char]

    # Join the list of characters back into a string and return it
    return "".join(char_list)
