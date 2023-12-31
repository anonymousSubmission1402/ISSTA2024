
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the characters and their ASCII values
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = ord(char)
    # Sort the dictionary by value (ASCII value)
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1])
    # Return the top n characters with the smallest ASCII values
    return [x[0] for x in sorted_dict[:n]]
