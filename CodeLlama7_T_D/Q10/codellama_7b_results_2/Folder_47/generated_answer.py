
def all_odd_ints_exclusive(my_list):
    # create a new list to store the odd integers
    odd_ints = []

    # loop through the list of integers, starting at index 64
    for i in range(64, len(my_list)):
        # if the current element is an odd integer, append it to the list of odd integers
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # return the list of all odd integers from index 64 to index 80, both exclusive
    return odd_ints
