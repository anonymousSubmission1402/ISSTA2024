
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for i in range(len(set) + 1):
        for j in range(i + 1, len(set) + 1):
            for k in range(j + 1, len(set) + 1):
                for l in range(k + 1, len(set) + 1):
                    # If the current combination is of size 4, increment the number of subsets
                    if len({i, j, k, l}) == 4:
                        num_subsets += 1

    # Return the number of all its subsets of size 4
    return num_subsets
