
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string
    indices = []
    for char in string:
        indices.append(string.index(char))

    # Sort the indices by the ASCII values of the corresponding characters
    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))

    # Return the 6th smallest ASCII value among the characters in the string that occur between indices 9 to 59, both inclusive
    return string[sorted_indices[8]:sorted_indices[10]]
