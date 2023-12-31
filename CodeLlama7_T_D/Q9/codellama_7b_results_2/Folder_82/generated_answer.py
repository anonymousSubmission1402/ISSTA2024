
def all_odd_ints_inclusive(my_list):
    # Get the length of the list
    list_length = len(my_list)
    # Initialize an empty list to store the odd integers
    odd_integers = []
    # Iterate through the list from index 20 to index 200
    for i in range(20, list_length):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list of odd integers
            odd_integers.append(my_list[i])
    # Return the list of all odd integers from index 20 to index 200, both inclusive
    return odd_integers
