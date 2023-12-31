
def all_odd_ints_inclusive(my_list):
    # Find the starting index of the range
    start_index = 36

    # Find the ending index of the range
    end_index = 46

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list and append the odd integers to the list
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 36 to index 46, both inclusive
    return odd_ints
