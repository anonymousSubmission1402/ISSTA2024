
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list and append each odd integer to the empty list
    for i in range(36, 54):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 36 to index 54, both exclusive
    return odd_ints
