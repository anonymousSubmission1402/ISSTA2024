
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between indices 46 and 82 (inclusive)
    indices = [i for i, c in enumerate(string) if 46 <= i <= 82]
    # Sort the indices by their corresponding ASCII values
    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))
    # Return the character with the 16th smallest ASCII value among those characters in the string that occur between indices 46 and 82 (inclusive)
    return string[sorted_indices[15]]
