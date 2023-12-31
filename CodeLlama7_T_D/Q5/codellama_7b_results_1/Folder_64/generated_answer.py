
def all_neg_ints_inclusive(my_list):
    # Create an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(len(my_list)):
        # If the current element is a negative integer, add it to the output list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the output list of negative integers
    return neg_ints
