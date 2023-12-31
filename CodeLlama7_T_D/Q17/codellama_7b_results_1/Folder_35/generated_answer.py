
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []
    # Loop through the specified range of the list
    for i in range(77, 87 + 1):
        # Check if the current integer is divisible by both 23 and 57
        if my_list[i] % 23 == 0 and my_list[i] % 57 == 0:
            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])
    # Return the list of divisible integers
    return divisible_integers
