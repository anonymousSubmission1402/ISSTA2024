
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Check if any element occurs at least once in both lists between index 80 and index 200
    for i in range(80, 201):
        if list1[i] in common_elements or list2[i] in common_elements:
            return common_elements
    # If no such elements exist, return an empty set
    return set()
