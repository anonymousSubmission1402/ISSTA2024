
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list from index 31 to index 34, both inclusive
    for i in range(31, 35):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            total += my_list[i]
    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return total
