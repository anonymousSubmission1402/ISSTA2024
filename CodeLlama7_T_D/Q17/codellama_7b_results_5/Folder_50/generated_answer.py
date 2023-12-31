
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate through the specified range of indices in my_list
    for i in range(46, 92):

        # Check if the current integer is divisible by both 67 and 15
        if my_list[i] % 67 == 0 and my_list[i] % 15 == 0:

            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
