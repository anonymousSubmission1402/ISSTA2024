
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list from index 30 to index 87, both inclusive
    for i in range(30, 88):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]
    # Return the sum of all even integers from index 30 to index 87, both inclusive. If no even integers exist in the specified range, return 0.
    return total
