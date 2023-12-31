
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 78
    end_index = 81

    # Iterate over the specified range of the list
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 76 or 60
        if my_list[i] % 76 == 0 or my_list[i] % 60 == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the total
    return total
