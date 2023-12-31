
def find_subset_of_length_n(elements):
    # Initialize the number of subsets to 0
    num_subsets = 0
    # Loop through all possible combinations of elements
    for combination in combinations(elements, n):
        # If the current combination has a length of 72, increment the number of subsets
        if len(combination) == 72:
            num_subsets += 1

    return num_subsets
