
def return_n_smallest_chars(string, n=82):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in string]
    # Sort the list in descending order based on the ASCII value
    sorted_char_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the top 82 characters in the list
    return [c for c, _ in sorted_char_list[:n]]
