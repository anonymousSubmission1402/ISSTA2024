
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 240
    end_index = 901
    # Iterate through the list and calculate the sum of all integers divisible by either 546 or 709
    for i in range(start_index, end_index + 1):
        if my_list[i] % 546 == 0 or my_list[i] % 709 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 546 or 709 from index 240 to index 901, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
