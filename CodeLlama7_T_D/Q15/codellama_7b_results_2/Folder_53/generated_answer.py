
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list from index 300 to index 300, both inclusive
    for i in range(300, 301):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
