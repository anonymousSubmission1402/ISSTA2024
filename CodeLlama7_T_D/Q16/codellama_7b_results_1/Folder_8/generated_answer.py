
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers starting from index 23, inclusive
    for i in range(23, len(my_list)):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 23 to index 23, inclusive. If no even integers exist in the specified range, return 0.
    return total
