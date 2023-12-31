
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list and check if each element is even
    for i in range(31, 72 + 1):
        if my_list[i] % 2 == 0:
            # If the element is even, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 31 to index 72, both inclusive
    return total
