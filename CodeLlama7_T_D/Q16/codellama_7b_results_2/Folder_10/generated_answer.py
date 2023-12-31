
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 25 and ending at index 59 (inclusive)
    for i in range(25, 60):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 25 to index 59 (inclusive), or 0 if no even integers exist in the specified range.
    return total
