
def identical_elements(list1, list2):
    # create a set of all elements that occur at least once in both lists between index 209 and 556, both inclusive
    common_elements = {element for element in set(list1[209:557]) & set(list2[209:557])}
    return common_elements
