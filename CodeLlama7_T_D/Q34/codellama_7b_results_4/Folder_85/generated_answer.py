
def find_original_set(sets):
    # create an empty set to store the original sets
    original_set = set()

    # loop through each of the given arguments
    for arg in sets:
        # add each element of the current argument to the original set
        for element in arg:
            original_set.add(element)

    return original_set
