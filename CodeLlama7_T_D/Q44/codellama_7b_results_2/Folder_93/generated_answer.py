
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Loop through the list of integers from index 23 to index 23, both inclusive
    for i in range(23, len(my_list)):
        # Check if the current element is divisible by any number between 1 and itself
        for j in range(1, my_list[i] + 1):
            if my_list[i] % j == 0:
                # If it is, add it to the set of composite numbers
                composite_numbers.add(my_list[i])

    return composite_numbers
