
def all_odd_ints_inclusive(my_list):
    # Define the start and end indices for the range of odd integers
    start = 82
    end = 86
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from the start index to the end index
    for i in range(start, end + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from the specified range, or an empty list if no odd integers exist in the range
    return odd_ints
