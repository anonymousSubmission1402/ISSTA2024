
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in the input list
    for i in range(29, 46):
        # Check if the current element is divisible by both 27 and 81
        if my_list[i] % 27 == 0 and my_list[i] % 81 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 27 and 81 from index 29 to index 45, both inclusive
    return divisible_ints
