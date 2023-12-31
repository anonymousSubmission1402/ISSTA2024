
def filter_chars(s):
    # Create a list of characters in the given string
    char_list = list(s)
    # Loop through each character in the list and check if it meets the criteria
    for i in range(len(char_list)):
        if (10 <= i <= 69) and ('I' <= char_list[i] <= 'K'):
            # If the character meets the criteria, remove all occurrences of that character from the string
            char_list = [c for c in char_list if c != char_list[i]]
    # Return the altered string
    return ''.join(char_list)
