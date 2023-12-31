
def return_nth_smallest_ascii(s):
    # Create a dictionary to store the character and its ASCII value
    char_dict = {}

    # Iterate through the string and create a dictionary of characters and their ASCII values
    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = ord(s[i])

    # Sort the dictionary by value (ASCII value) in ascending order
    sorted_dict = dict(sorted(char_dict.items(), key=lambda x: x[1]))

    # Return the character with the 7th smallest ASCII value
    return sorted_dict[list(sorted_dict.keys())[6]]
