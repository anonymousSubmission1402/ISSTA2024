
def find_subset_of_length_n(set):
    # Initialize a counter for the number of subsets
    count = 0

    # Iterate over all possible combinations of elements in the set
    for i in range(1 << len(set))):
        # Create a subset from the current combination
        subset = []
        for j in range(len(set)):
            if i & (1 << j)):
                subset.append(set[j])

        # Check if the subset has size 6
        if len(subset) == 6:
            count += 1

    # Return the number of subsets of size 6
    return count
