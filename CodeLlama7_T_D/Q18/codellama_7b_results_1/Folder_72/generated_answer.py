
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 38
    end_index = 81
    # Loop through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either -61 or -71
        if my_list[i] % (-61) == 0 or my_list[i] % (-71) == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    return sum
