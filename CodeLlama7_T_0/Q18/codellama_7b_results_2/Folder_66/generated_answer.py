
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 58
    end_index = 81
    # Iterate through the list and calculate the sum of all integers divisible by either 55 or 10
    for i in range(start_index, end_index + 1):
        if my_list[i] % 55 == 0 or my_list[i] % 10 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 55 or 10 from index 58 to index 81, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
