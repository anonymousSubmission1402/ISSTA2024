
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 154
    end_index = 798
    # Iterate through the list and calculate the sum of all integers divisible by either 275 or 580 from index 154 to index 798, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % 275 == 0 or my_list[i] % 580 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 275 or 580 from index 154 to index 798, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
