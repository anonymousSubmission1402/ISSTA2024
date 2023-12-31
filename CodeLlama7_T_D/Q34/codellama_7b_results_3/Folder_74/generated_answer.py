
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over each element in the input list and compare it with the current smallest set

    for i in range(1, len(sets)):
        if len(smallest_set.intersection(sets[i])) < len(smallest_set):
            smallest_set = sets[i]

    return smallest_set
