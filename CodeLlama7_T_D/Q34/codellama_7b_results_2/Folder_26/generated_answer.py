
def find_original_set(sets):
    # Find the smallest set in the input list
    smallest_set = sets[0]
    for set in sets:
        if len(set) < len(smallest_set):
            smallest_set = set

    return smallest_set
