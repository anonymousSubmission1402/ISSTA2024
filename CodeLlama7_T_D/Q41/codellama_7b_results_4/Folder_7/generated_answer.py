
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the final result
    final_result = set()
    # Iterate through each element in the set of common elements
    for element in common_elements:
        # Check if the element occurs at least once in both lists between indices 661 and 924 (inclusive)
        if list1.count(element) >= 661 and list2.count(element) >= 661 and \
                    list1.index(element) <= 924 and list2.index(element) <= 924:
            # If the element occurs at least once in both lists between indices 661 and 924 (inclusive), add it to the final result set
            final_result.add(element)
    # Return the final result set of all elements that occur at least once in both lists between indices 661 and 924 (inclusive), or an empty set if no such elements exist in the given lists.
    return final_result
