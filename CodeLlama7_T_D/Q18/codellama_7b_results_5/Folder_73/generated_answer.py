 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range and the divisors
    start = 81
    end = 86
    div_33 = -33
    div_62 = -62
    # Initialize an empty list to store the divisible integers
    divisible_ints = []
    # Loop through the range of indices and check if each integer is divisible by either -33 or -62
    for i in range(start, end + 1):
        if my_list[i] % div_33 == 0 or my_list[i] % div_62 == 0:
            # If the integer is divisible by either -33 or -62, add it to the list of divisible integers
            divisible_ints.append(my_list[i])
    # Return the sum of all integers in the specified range that are divisible by either -33 or -62
    return sum(divisible_ints)
