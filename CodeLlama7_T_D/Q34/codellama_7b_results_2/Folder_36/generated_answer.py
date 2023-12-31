
def find_original_set(sets):
    # Find the smallest set that contains all the given sets
    smallest_set = None
    for s in sets:
        if smallest_set is None:
            smallest_set = s
        else:
            smallest_set = smallest_set.union(s)
    return smallest_set
