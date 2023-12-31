
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_negative = next((i for i in my_list if i < 0), None)
    # If there are no negative integers in the list, return an empty list
    if first_negative is None:
        return []

    # Find the last negative integer in the list
    last_negative = next(reversed(my_list), None)
    # If there are no negative integers in the list, return an empty list
    if last_negative is None:
        return []

    # Return a list of all negative integers from index 22 to index 24, both exclusive
    return [i for i in my_list[22:24] if i < 0]
