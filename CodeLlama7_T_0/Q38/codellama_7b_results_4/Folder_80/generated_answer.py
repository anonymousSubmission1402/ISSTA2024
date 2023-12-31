
def find_subset_of_length_n(my_set):
    # Initialize a variable to keep track of the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for combination in itertools.combinations(my_set, 36):
        # If the current combination is valid (i.e., it has exactly 36 elements), increment the number of subsets
        if len(combination) == 36:
            num_subsets += 1

    # Return the final number of subsets
    return num_subsets
