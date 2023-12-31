
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list of integers
    for i in range(10):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            sum += my_list[i]
    # Return the sum of all odd integers from index 0 to index 10, both inclusive
    return sum
