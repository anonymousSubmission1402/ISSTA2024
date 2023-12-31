
def all_ints_div_by_num(my_list):
    # create a new list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of the input list
    for i in range(10, 52 + 1):
        # check if the current element is divisible by -12
        if my_list[i] % -12 == 0:
            # if it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # return the list of all divisible integers from index 10 to index 52, both inclusive
    return divisible_ints
