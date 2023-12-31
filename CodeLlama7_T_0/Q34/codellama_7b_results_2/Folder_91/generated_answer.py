
def find_original_set(set1, set2, set3, set4, set5):
    # Create a list of all the given sets
    sets = [set1, set2, set3, set4, set5]
    # Initialize an empty set to store the smallest set
    smallest_set = set()

    # Iterate through each set in the list and add its elements to the smallest set
    for s in sets:
        smallest_set |= s

    return smallest_set
