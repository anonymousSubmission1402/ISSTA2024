
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 48
    end_index = 59

    # Iterate through the list and calculate the sum of all integers divisible by either 88 or 58
    for i in range(start_index, end_index + 1):
        if my_list[i] % 88 == 0 or my_list[i] % 58 == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either 88 or 58 from index 48 to index 59, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
