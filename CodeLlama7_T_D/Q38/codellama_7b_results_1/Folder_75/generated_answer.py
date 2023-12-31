
def find_subset_of_length_n(set):
    # Initialize the number of subsets to 0
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for subset in itertools.combinations(set, 80):
        # Increment the number of subsets by 1
        num_subsets += 1

    # Return the number of subsets of size 80
    return num_subsets
