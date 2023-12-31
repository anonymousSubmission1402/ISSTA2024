
def all_neg_ints_exclusive(my_list):
    # Get the range of indices where negative integers exist
    neg_int_indices = [i for i, x in enumerate(my_list) if x < 0]
    # Check if any negative integers exist in the specified range
    if len(neg_int_indices) == 0:
        return []

    # Get the list of all negative integers from index 42 to index 87, both exclusive
    neg_ints = my_list[neg_int_indices[42]:neg_int_indices[87]]
    return neg_ints
