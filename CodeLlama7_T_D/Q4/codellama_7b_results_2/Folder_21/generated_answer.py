
def all_pos_ints_exclusive(my_list):
    # Get the range of positive integers in the list
    pos_int_range = range(743, 867)
    # Check if any positive integers exist in the specified range
    if not any(x > 0 for x in my_list[pos_int_range]):
        return []

    else:

        # Return the list of all positive integers from index 743 to index 867, both exclusive
        return [x for x in my_list[pos_int_range] if x > 0]
