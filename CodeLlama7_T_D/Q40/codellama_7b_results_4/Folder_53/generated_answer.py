
def return_n_smallest_chars(my_string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string)
    # create a list of exactly 19 characters from the sorted string
    smallest_chars = sorted_string[:19]
    return smallest_chars
