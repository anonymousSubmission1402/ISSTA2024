
def return_n_smallest_chars(string, n):
    # Sort the string in ascending order
    sorted_string = sorted(string)

    # Create a list of exactly n smallest characters
    smallest_chars = []
    for i in range(n):
        smallest_chars.append(sorted_string[i])

    # Return the list of smallest characters
    return smallest_chars
