
def find_original_set(sets):
    # Create a list of all elements in the sets
    all_elements = []
    for s in sets:
        all_elements += list(s)
    # Sort the list of all elements
    all_elements.sort()
    # Initialize an empty set to store the smallest set
    smallest_set = set()
    # Iterate through each element and add it to the smallest set
    for e in all_elements:
        smallest_set.add(e)
    return smallest_set
