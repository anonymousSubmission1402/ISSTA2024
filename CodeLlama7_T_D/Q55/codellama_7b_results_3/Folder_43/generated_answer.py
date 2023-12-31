
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its index
        current_element = circular_list[i]
        current_index = i

        # Initialize a product variable to store the product of the sublist elements
        product = 1

        # Loop through the remaining elements of the circular list starting from the current index
        for j in range(current_index + 1, len(circular_list)):
            # Get the next element and its index
            next_element = circular_list[j]
            next_index = j

            # Update the product variable with the product of the current element and the next element
            product *= next_element

            # If the product is equal to -26, add the sublist containing the current and next elements to the list of sublists
            if product == -26:
                sublists.append(circular_list[current_index:next_index + 1])

    # Return the list of sublists
    return sublists
