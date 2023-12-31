
def all_neg_ints_inclusive(my_list):
    # Find the first negative integer in the list
    first_negative_index = next((i for i, x in enumerate(my_list) if x < 0)), None)
    # If no negative integers exist in the specified range, return an empty list
    if first_negative_index is None:
        return []

    # Find the last negative integer in the list

    last_negative_index = next((i for i in range(first_negative_index, len(my_list)) if my_list[i] < 0)), None)
    # Return the list of all negative integers from index 56 to index 98, both inclusive
    return my_list[first_negative_index:last_negative_index+1]
