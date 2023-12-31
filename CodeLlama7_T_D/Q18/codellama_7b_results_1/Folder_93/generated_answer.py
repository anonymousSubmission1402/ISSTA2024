
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list from index 86 to 89 (both inclusive)
    for i in range(86, 90):
        # Check if the current element is divisible by either -61 or -79
        if my_list[i] % -61 == 0 or my_list[i] % -79 == 0:
            # If it is, add it to the sum
            total += my_list[i]
    # Return the sum
    return total
