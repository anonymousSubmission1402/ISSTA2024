
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    i = 14
    # Loop through the list, starting from index 14
    while i <= 93:
        # If the current element is divisible by either 71 or 81
        if my_list[i] % 71 == 0 or my_list[i] % 81 == 0:
            # Add it to the sum
            sum += my_list[i]
        # Increment the current index
        i += 1
    return sum
