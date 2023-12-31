
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its neighbors
        current_element = circular_list[i]
        previous_element = None
        next_element = None

        if i > 0:
            previous_element = circular_list[i - 1]

        if i < len(circular_list) - 1:
            next_element = circular_list[i + 1]

        # Check if the current element is part of a sublist with product equal to -6
        if (current_element * previous_element * next_element) == -6:
            # Add the sublist to the list of sublists
            sublists.append([previous_element, current_element, next_element])

    return sublists
