
def find_original_set(sets):
    # Create a set to store all elements
    all_elements = set()

    # Iterate over the given sets and add all elements to the all_elements set
    for s in sets:
        all_elements.update(s)

    # Initialize an empty set as the smallest set
    smallest_set = set()

    # Iterate over the all_elements set and add only those elements that are present in all given sets to the smallest_set
    for element in all_elements:
        if all(element in s for s in sets):
            smallest_set.add(element)

    # Return the smallest_set as the original set
    return smallest_set
