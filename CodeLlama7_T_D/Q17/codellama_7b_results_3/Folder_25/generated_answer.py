
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result_list = []
    # Iterate through the list of integers from index 25 to index 80, both inclusive
    for i in range(25, 81):
        # Check if the current integer is divisible by both -20 and -26
        if my_list[i] % -20 == 0 and my_list[i] % -26 == 0:
            # If it is, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
