
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list from index 1 to index 8 (both inclusive)
    for i in range(1, len(my_list)):
        # Check if the current element is odd
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 1 to index 8 (both inclusive)
    return odd_ints
