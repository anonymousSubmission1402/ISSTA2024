
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the number is between 11 and 76, both inclusive
        if 11 <= num <= 76:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
