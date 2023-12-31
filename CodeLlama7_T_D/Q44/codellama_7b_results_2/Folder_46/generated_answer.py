
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list from index 28 to 38 (both inclusive)
    for i in range(28, 39):
        # Check if the current element is a prime number
        if my_list[i] == 1:
            # If it is a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 28 and index 38 (both inclusive), or an empty set if no composite number exists in the specified range
    return composite_nums
