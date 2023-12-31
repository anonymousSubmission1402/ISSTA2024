
def all_odd_ints_inclusive(my_list):
    # Define start and end indices for the range of odd integers
    start = 62
    end = 63
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list from the start index to the end index
    for i in range(start, end+1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 62 to index 63, both inclusive
    return odd_ints
