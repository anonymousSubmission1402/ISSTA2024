
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the specified range of the input list
    for i in range(389, 748):
        # Check if the current element is negative
        if my_list[i] < 0:
            # Add the negative integer to the output list
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 389 to index 748, both exclusive
    return neg_ints
