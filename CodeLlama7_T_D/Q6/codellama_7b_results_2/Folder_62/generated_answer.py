
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    for i, x in enumerate(my_list):
        if x < 0:
            first_negative = i
            break

    # If no negative integers exist in the list, return an empty list
    if first_negative is None:
        return []

    # Find the last negative integer in the list

    for i in range(first_negative, len(my_list)):
        if my_list[i] < 0:
            last_negative = i
            break

    # Return the list of all negative integers from index first_negative to index last_negative, both exclusive
    return my_list[first_negative:last_negative]
