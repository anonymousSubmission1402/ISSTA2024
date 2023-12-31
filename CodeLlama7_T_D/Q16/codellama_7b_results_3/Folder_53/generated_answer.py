
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list of integers, starting from index 111 and ending at index 111 (both inclusive)
    for i in range(111, 112):
        # If the current integer is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]

    # Return the sum of all even integers from index 111 to index 111 (both inclusive), or 0 if no even integers exist in the specified range.
    return sum
