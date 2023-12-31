
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list from index 22 to index 63, both inclusive
    for i in range(22, 64):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 22 to index 63, both inclusive
    return total
