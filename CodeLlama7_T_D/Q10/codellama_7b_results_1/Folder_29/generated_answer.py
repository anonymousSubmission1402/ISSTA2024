
def all_odd_ints_exclusive(my_list):
    # Find the starting index of the range
    start_index = 48

    # Find the ending index of the range
    end_index = 76

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list and append the odd integers to the 'odd_ints' list
    for i in range(start_index, end_index):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 48 to index 76, both exclusive
    return odd_ints
