
def return_n_smallest_chars(string, n):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(string, key=ord, reverse=True)
    # Return the top 82 characters from the sorted string
    return sorted_string[:n]
