
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list, starting from index 50 and ending at index 200 (both inclusive)
    for i in range(50, 201):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # If it is even, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
