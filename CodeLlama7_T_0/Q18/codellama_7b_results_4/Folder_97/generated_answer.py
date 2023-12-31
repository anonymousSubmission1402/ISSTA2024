
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 58
    end_index = 75

    # Iterate through the list and calculate the sum of all integers divisible by either 72 or 62
    for i in range(start_index, end_index + 1):
        if my_list[i] % 72 == 0 or my_list[i] % 62 == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either 72 or 62 from index 58 to index 75, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
