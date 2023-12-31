
def identical_elements(list1, list2):
    # create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # initialize an empty set to store the results
    matching_elements = set()

    # iterate over the common elements and check if they are present at least once in both lists between indices 661 and 924, inclusive
    for element in common_elements:
        count1 = list1.count(element)
        count2 = list2.count(element)

        # if the element is present at least once in both lists between indices 661 and 924, inclusive, add it to the set of matching elements
        if count1 >= 1 and count2 >= 1:
            for i in range(len(list1)):
                if list1[i] == element:
                    for j in range(661, 924 + 1):
                        if list2[j] == element:
                            matching_elements.add(element)

    # return the set of matching elements

    return matching_elements
