
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 315
    end_index = 934
    divisible_ints = []

    # Iterate over the list and append
    # integers that are divisible by either -897 or -556
    for i in range(start_index, end_index + 1):
        if my_list[i] % -897 == 0 or my_list[i] % -556 == 0:
            divisible_ints.append(my_list[i])

    # Return the sum of the divisible integers
    return sum(divisible_ints)
