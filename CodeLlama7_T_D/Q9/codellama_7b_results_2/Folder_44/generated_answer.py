
def all_odd_ints_inclusive(my_list):
    # initialize an empty list to store the odd integers
    odd_ints = []
    # loop through the specified range of indices in my_list
    for i in range(13, 68+1):
        # check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # if it is, append it to the list of odd integers
            odd_ints.append(my_list[i])
    # return the list of all odd integers from index 13 to index 68, both inclusive
    return odd_ints
