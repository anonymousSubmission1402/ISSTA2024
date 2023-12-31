
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list of integers starting from index 14 to index 68, both inclusive
    for i in range(14, 69):
        # Check if the current integer is divisible by 18
        if my_list[i] % 18 == 0:
            # If the current integer is divisible by 18, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 18 from index 14 to index 68, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
