
def find_original_set(sets):
    # Find the smallest set that contains all the given sets
    smallest_set = sets[0]
    for i in range(1, len(sets)):
        if len(smallest_set) > len(sets[i])):
            smallest_set = sets[i]

    return smallest_set
