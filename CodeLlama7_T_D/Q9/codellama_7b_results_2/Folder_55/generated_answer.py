
def all_odd_ints_inclusive(my_list):
    # Find the starting index of the range
    start_index = 10

    # Find the ending index of the range
    end_index = min(start_index + 10, len(my_list))

    # Create an empty list to store the odd integers
    odd_ints = []

    # Loop through the specified range and append any odd integers to the list
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from the specified range
    return odd_ints
