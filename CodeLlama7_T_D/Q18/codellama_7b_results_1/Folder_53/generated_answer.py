
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate over the list, starting from index 200
    for i in range(200, len(my_list)):
        # Check if the current element is divisible by either 17 or -5
        if my_list[i] % 17 == 0 or my_list[i] % -5 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
