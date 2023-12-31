
def return_nth_smallest_ascii(string):
    # Get the indices of all characters in the string
    char_indices = {}
    for i, char in enumerate(string):
        if char not in char_indices:
            char_indices[char] = []
        char_indices[char].append(i)
    # Get the ASCII values of all characters between indices 51 and 78
    ascii_values = {}
    for char, indices in char_indices.items():
        if len(indices) > 0:
            min_index = min(indices)
            max_index = max(indices)
            if min_index >= 51 and max_index <= 78:
                ascii_values[char] = ord(char)
    # Return the character with the 9th smallest ASCII value
    return sorted(ascii_values.items(), key=lambda x: x[1])[8][0]
