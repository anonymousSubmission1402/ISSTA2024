
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between 8 and 9, both inclusive
        if 8 <= i <= 9:
            # Add the current integer to the sum variable
            sum += i

    # Return the sum of all integers from the given list that are between 8 and 9, both inclusive
    return sum
