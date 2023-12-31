
def find_original_set(sets):
    # Check if all sets are non-empty and have the same size
    if len(sets) == 0 or any(len(s) == 0 for s in sets)):
        raise ValueError("All sets must be non-empty")

    # Initialize the smallest set as the first set
    smallest_set = sets[0]

    # Iterate over all sets and find the smallest set that contains all elements of the current set
    for i in range(1, len(sets)):
        if all(element in smallest_set for element in sets[i]):
            smallest_set = sets[i]

    return smallest_set
