
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the desired elements
    desired_elements = set()
    # Iterate over each element in both lists
    for element in common_elements:
        # Check if the element is present at least once in both lists between index 28 and 40, inclusive
        if element in list1[28:41] and element in list2[28:41]:
            # If it is present, add it to the desired elements set
            desired_elements.add(element)
    # Return the desired elements set
    return desired_elements
