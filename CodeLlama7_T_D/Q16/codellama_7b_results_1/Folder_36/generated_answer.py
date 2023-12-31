
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list from index 246 to index 750, both inclusive
    for i in range(246, 751):

        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:

            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum
    return total
