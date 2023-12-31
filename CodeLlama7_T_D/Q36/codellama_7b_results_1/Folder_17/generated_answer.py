 def filter_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Iterate through each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between 18 and 95 (exclusive)
        if 17 < ord(char_list[i]) < 96:
            # If it is, check if it is greater than 'K' and smaller than 'a'
            if char_list[i] > 'K' and char_list[i] < 'a':
                # Remove all occurrences of the current character in the list
                char_list.remove(char_list[i])
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
