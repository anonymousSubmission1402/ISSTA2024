
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate over the two lists simultaneously
    for i in range(6, 9):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])

    return common_elements
