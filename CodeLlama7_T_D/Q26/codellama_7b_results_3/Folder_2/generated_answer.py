
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list of integers
    for i in my_list:
        # Check if the integer is between 266 and 586
        if 266 <= i <= 586:
            # Add the integer to the sum variable
            sum += i

    # Return the sum of all integers between 266 and 586 in the given list
    return sum
