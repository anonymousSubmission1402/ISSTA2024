
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:

        # Check if the current integer is between 584 and 619, both inclusive
        if 584 <= num <= 619:

            # If it is, add it to the total
            total += num

    # Return the total sum
    return total
