
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of the input list
    for i in range(32, 100 + 1):
        # check if the current integer is divisible by both -11 and -15
        if my_list[i] % (-11) == 0 and my_list[i] % (-15) == 0:
            # if it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # return the list of all integers divisible by both -11 and -15 from index 32 to index 99, both inclusive
    return divisible_ints
