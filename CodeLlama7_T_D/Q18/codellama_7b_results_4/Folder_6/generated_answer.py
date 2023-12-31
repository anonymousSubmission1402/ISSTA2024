
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 41
    end_index = 56
    # Iterate over the list in range [start_index, end_index]
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 82 or 90
        if my_list[i] % 82 == 0 or my_list[i] % 90 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
