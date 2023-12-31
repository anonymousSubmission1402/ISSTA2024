
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    for i in range(len(my_list)):
        # Check if current element is divisible by either 6 or -3
        if my_list[i] % 6 == 0 or my_list[i] % (-3) == 0:
            # Add current element to sum
            sum += my_list[i]
    return sum
