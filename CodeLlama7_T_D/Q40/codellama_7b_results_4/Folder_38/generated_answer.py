
def return_n_smallest_chars(string, n=45):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # Return the first n characters of the sorted string
    return sorted_string[:n]
