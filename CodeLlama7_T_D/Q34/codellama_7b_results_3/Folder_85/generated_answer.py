
def find_original_set(sets):
    # Create a set of all elements from the given sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # Initialize the smallest set with the first element

    smallest_set = {all_elements.pop()}

    # While there are still elements left to be added

    while all_elements:

        # Find the smallest element that is not in any of the existing sets

        smallest_element = None
        for e in all_elements:
            if e not in smallest_set:
                smallest_element = e
                break

        # If no such element was found, then there are no more elements to be added

        if smallest_element is None:
            break

        # Add the smallest element to the smallest set

        all_elements.remove(smallest_element)
        smallest_set.add(smallest_element)

    return smallest_set
