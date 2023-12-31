
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 543
    end_index = 584
    # Loop through the list and calculate the sum of all integers divisible by either -553 or -737 from index 543 to index 584, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % -553 == 0 or my_list[i] % -737 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
