
def all_neg_ints_exclusive(my_list):
    # Create a new list to store the negative integers
    neg_ints = []

    # Iterate through the list and append any negative integers to the new list
    for i in range(len(my_list)):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the new list of negative integers
    return neg_ints
