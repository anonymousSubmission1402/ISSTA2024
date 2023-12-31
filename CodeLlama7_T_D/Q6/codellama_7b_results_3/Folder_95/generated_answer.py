
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list from index 25 to index 80, exclusive
    for i in range(25, 80):
        # If the current element is a negative integer, add it to the neg_ints list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    # Return the neg_ints list
    return neg_ints
