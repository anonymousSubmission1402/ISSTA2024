
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list from index 25 to index 87, both inclusive
    for i in range(25, 88):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]
    # Return the sum of all odd integers from index 25 to index 87, both inclusive
    return total
