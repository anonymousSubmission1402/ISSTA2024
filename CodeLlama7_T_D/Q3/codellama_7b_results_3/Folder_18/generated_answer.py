
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Loop through the specified range of indices in 'my_list'
    for i in range(35, 49 + 1):

        # If the current index contains a positive integer, append it to 'pos_ints'
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from the specified range, or an empty list if no such integers exist
    return pos_ints
