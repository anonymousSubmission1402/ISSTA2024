
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 22
    end_index = 50
    # Iterate through the list from the starting index to the ending index
    for i in range(start_index, end_index + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            sum += my_list[i]
    # Return the sum of all odd integers from the specified range, or 0 if no such elements exist
    return sum
