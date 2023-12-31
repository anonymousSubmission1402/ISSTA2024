
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its successor
        curr_element = circular_list[i]
        succ_element = circular_list[(i+1) % len(circular_list)]

        # Check if the product of the current element and its successor is equal to -5
        if curr_element * succ_element == -5:
            # Add the sublist containing the current element and its successor to the list of sublists
            sublists.append([curr_element, succ_element])

    # Return the list of sublists
    return sublists
