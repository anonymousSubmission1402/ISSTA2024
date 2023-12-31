
def all_even_ints_exclusive(my_list):
    # Get the range of even integers from index 20 to index 93, both exclusive
    even_ints = my_list[20:93:2]
    # If no even integers exist in the specified range, return an empty list
    if not even_ints:
        return []

    # Otherwise, return the list of all even integers from index 20 to index 93, both exclusive
    return even_ints
