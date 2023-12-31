
def all_neg_ints_inclusive(my_list):
    # Create a new list to store the negative integers
    neg_ints = []
    # Loop through the specified range of indices in my_list
    for i in range(60, 201):
        # Check if the current element is negative
        if my_list[i] < 0:
            # Add the negative integer to the neg_ints list
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 60 to index 200, both inclusive
    return neg_ints
