
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 41
    end_index = 56
    # Loop through the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 82 == 0 or my_list[i] % 90 == 0:
            sum += my_list[i]
    return sum
