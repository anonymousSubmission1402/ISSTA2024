
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of the input list
    for i in range(27, 86 + 1):

        # Check if the current element is divisible by 29
        if my_list[i] % 29 == 0:

            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers from index 27 to index 86, both inclusive
    return divisible_ints
