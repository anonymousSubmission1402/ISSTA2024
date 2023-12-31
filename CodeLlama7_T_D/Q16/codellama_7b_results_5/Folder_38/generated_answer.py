
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list of integers from index 22 to index 63, both inclusive
    for i in range(22, 64):
        # If current element is even, add it to sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return sum of all even integers from index 22 to index 63, both inclusive
    return sum
