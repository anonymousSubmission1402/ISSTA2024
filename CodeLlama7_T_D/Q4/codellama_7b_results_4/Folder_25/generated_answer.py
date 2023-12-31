
def all_pos_ints_exclusive(my_list):
    # Get the indices of the first and last positive integers in the list
    start_idx = next((i for i, x in enumerate(my_list) if x > 0), None)
    end_idx = next((i for i, x in reversed(list(enumerate(my_list)))))
    # If no positive integers exist in the list, return an empty list
    if start_idx is None or end_idx is None:
        return []

    # Return the list of all positive integers from index 41 to index 69, both exclusive
    return my_list[start_idx:end_idx]
