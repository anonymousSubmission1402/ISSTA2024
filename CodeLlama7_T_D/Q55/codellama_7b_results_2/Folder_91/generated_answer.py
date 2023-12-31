
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list
    for i in range(len(circular_list)):

        # Get the current element and its successor
        current_element = circular_list[i]
        next_element = circular_list[(i+1) % len(circular_list)]

        # Check if the product of the current element and its successor is equal to 2
        if current_element * next_element == 2:

            # Add the sublist containing the current element and its successor to the list of sublists
            sublists.append([current_element, next_element])

    # Return the list of sublists
    return sublists
