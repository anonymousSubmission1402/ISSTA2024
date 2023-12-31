
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list and find all odd integers in the specified range
    for i in range(3, 6):
        if my_list[i] % 2 != 0:
            # Add the odd integer to the total
            total += my_list[i]

    # Return the sum of all odd integers found in the specified range
    return total
