
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 35 and 49, inclusive
    for element in common_elements:
        count1 = list1.count(element)
        count2 = list2.count(element)
        # If the element occurs at least once in both lists between index 35 and 49, inclusive, add it to the result set
        if (count1 > 0 and count2 > 0) and (count1 + count2 >= 36 and count1 + count2 <= 50):
            result.add(element)
    # Return the set of identical elements
    return result
