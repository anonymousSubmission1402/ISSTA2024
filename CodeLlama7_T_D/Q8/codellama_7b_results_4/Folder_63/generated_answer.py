
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list of integers starting from index 38 (inclusive) and ending at index 52 (exclusive)
    for i in range(38, 52):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 38 to index 52, both exclusive
    return even_ints
