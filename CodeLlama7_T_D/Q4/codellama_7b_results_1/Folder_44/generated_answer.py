
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate over the input list and check if each element is a positive integer
    for i in range(81, 86):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 81 to index 86, both exclusive
    return pos_ints
