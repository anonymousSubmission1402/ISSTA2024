
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the input list and append any negative integers to the output list
    for i in range(len(my_list)):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    return neg_ints
