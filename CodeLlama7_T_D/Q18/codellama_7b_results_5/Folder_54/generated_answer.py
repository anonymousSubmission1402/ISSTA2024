
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the start and end indices of the range we want to check
    start = 13
    end = 91
    # Initialize a variable to keep track of the sum of the divisible integers
    sum = 0
    # Iterate through the list from start to end
    for i in range(start, end + 1):
        # Check if the current element is divisible by either -65 or -62
        if my_list[i] % (-65) == 0 or my_list[i] % (-62) == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum of the divisible integers
    return sum
