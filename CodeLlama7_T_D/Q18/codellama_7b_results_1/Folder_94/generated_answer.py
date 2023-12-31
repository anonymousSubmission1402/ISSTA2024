
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 93
    end_index = 94

    # Check if the list is long enough to include the desired range
    if len(my_list) < (end_index + 1):
        return 0

    # Iterate through the specified range and add up all integers divisible by either -53 or -91
    for i in range(start_index, end_index + 1):
        if my_list[i] % -53 == 0 or my_list[i] % -91 == 0:
            total += my_list[i]

    # Return the sum
    return total
