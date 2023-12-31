
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from index 55 to index 84, both exclusive
    for i in range(55, 84):
        # If the current element is negative, add it to the list of negative integers
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
