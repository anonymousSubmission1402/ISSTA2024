
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(10, 76 + 1):
        # Check if the current integer is divisible by both -40 and -12
        if my_list[i] % (-40) == 0 and my_list[i] % (-12) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -40 and -12 from index 10 to index 76, both inclusive
    return divisible_ints
