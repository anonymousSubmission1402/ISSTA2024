
def all_pos_ints_inclusive(my_list):
    # Find the starting and ending indices of the positive integers in the list
    start_idx = None
    end_idx = None
    for i, x in enumerate(my_list):
        if x > 0:
            if start_idx is None:
                start_idx = i

            end_idx = i

    # Return an empty list if no positive integers exist in the specified range

    if start_idx is None:
        return []

    # Return the list of all positive integers from index 527 to index 538, both inclusive

    return my_list[start_idx:end_idx+1]
