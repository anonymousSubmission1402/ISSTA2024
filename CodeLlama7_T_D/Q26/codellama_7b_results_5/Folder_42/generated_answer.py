
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:

        # Check if the current integer is between 141 and 262, both inclusive
        if 141 <= num <= 262:

            # If it is, add it to the total
            total += num

    # Return the sum of all integers between 141 and 262
    return total
