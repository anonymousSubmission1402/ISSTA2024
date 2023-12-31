 def return_n_smallest_chars(string, n=2):
    # Sort the characters in the string based on their ASCII values
    sorted_characters = sorted(string, key=ord)
    # Return the first n characters of the sorted list
    return sorted_characters[:n]
