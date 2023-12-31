
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers, starting from index 66 and ending at index 93
    for i in range(66, 94):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum of all even integers in the specified range, or 0 if no such integers exist.
    return total
