
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers, starting from index 25 and ending at index 87 (inclusive)
    for i in range(25, 88):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is an even integer, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 25 to index 87 (inclusive), or an empty list if no even integers exist in the specified range
    return even_ints
