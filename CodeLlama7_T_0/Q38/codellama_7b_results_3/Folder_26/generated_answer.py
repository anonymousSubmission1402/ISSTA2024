
def find_subset_of_length_n(set):
    # Initialize a counter for the number of subsets
    count = 0

    # Iterate over all possible combinations of elements in the set
    for i in range(len(set)):
        for j in range(i + 1, len(set)):
            # If the current combination is of size 25, increment the counter
            if len({*set[i], *set[j]}) == 25:
                count += 1

    # Return the number of subsets of size 25
    return count
