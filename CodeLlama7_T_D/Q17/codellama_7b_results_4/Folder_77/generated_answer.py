
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers starting from index 828
    for i in range(828, len(my_list)):
        # Check if the current integer is divisible by both -649 and -461
        if my_list[i] % (-649 * -461) == 0:
            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -649 and -461 from index 828 to index 932, both inclusive
    return divisible_ints
