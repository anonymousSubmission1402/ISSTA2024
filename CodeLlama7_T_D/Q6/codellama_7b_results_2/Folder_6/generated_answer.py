
def all_neg_ints_exclusive(my_list):
    # initialize an empty list to store the negative integers
    neg_ints = []
    # loop through the list of integers starting from index 86
    for i in range(86, len(my_list)):
        # check if the current element is a negative integer
        if my_list[i] < 0:
            # add the current element to the list of negative integers
            neg_ints.append(my_list[i])
    return neg_ints
