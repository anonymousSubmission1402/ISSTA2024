
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list from index 62 to index 92, both inclusive
    for i in range(62, 93):

        # If the current element is a negative integer, append it to the neg_ints list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the neg_ints list
    return neg_ints
