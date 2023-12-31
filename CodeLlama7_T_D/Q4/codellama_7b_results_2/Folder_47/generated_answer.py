
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_positive = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # If no positive integers exist in the specified range, return an empty list
    if first_positive is None:
        return []

    # Find the last positive integer in the list

    last_positive = next((i for i, x in enumerate(my_list[first_positive:]) if x > 0)), None)
    # Return the list of all positive integers from index 64 to index 80, both exclusive

    return my_list[first_positive:last_positive+1]
