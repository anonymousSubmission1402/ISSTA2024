
def all_even_ints_exclusive(my_list):
    # Create a slice of the list starting at index 86 and ending at index 90 (exclusive)
    even_ints = my_list[86:90]
    # Filter out any odd integers from the slice
    filtered_ints = [x for x in even_ints if x % 2 == 0]
    return filtered_ints
