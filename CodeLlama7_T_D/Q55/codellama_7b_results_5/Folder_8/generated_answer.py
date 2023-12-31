
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Iterate over the elements of the current sublist
        for j in range(i, len(circular_list)):
            # Update the product of the elements in the current sublist
            product *= circular_list[j]

            # Check if the product equals -41
            if product == -41:
                # Add the current sublist to the list of sublists
                sublists.append(circular_list[i:j+1])

                # Break out of the inner loop since we have found a sublist with a product equal to -41
                break

        # Check if we have found a sublist with a product equal to -41
        if len(sublists) > 0:
            # Return the list of sublists
            return sublists

    # If we reach this point, it means that no sublist exists in the given circular list with a product equal to -41. Therefore, we return an empty list.
    return []
