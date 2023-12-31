
def lists_with_product_equal_n(circular_list):
    # Create an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its previous neighbor
        product = 1

        # Iterate over the previous neighbors of the current element
        for j in range(i-1, -1, -1):
            # Multiply the product by the current element and its previous neighbor
            product *= circular_list[j]

            # If the product is equal to -65, add the sublist containing the current element and its previous neighbors to the list of sublists
            if product == -65:
                sublists.append(circular_list[i-1:i+1])

        # Reset the product to 1 for the next iteration
        product = 1

    # Return the list of sublists containing the contiguous integers from the given circular list such that their product equals -65
    return sublists
