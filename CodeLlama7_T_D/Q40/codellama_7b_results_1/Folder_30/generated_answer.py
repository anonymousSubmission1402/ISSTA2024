
def return_n_smallest_chars(string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # return the first 72 characters of the sorted string
    return sorted_string[:72]
