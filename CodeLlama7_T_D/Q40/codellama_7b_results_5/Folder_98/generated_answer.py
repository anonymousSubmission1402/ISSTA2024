 def return_n_smallest_chars(string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # Extract the first 68 characters from the sorted string
    smallest_chars = sorted_string[:68]
    # Return the list of smallest characters in descending order
    return list(reversed(smallest_chars))
