
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 78 and 81 (both exclusive)
        if 78 < i < 81:
            # Check if the current character is greater than 'S' and smaller than '['
            if char_list[i] > 'S' and char_list[i] < '[':
                # Remove all occurrences of the current character from the list
                while char_list[i] in char_list:
                    char_list.remove(char_list[i])

    # Join the list of characters back into a string and return it
    return ''.join(char_list)
