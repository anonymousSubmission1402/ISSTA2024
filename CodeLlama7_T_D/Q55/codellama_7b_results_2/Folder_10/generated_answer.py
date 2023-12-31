
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers with a product equal to -93
    for i in range(len(circular_list)):
        # Calculate the product of the current element and the next element (if it exists)
        prod = circular_list[i] * (circular_list[(i + 1) % len(circular_list)] if (i + 1) % len(circular_list) else None)

        # If the product is equal to -93, add the sublist to the list of sublists
        if prod == -93:
            sublists.append([circular_list[i], circular_list[(i + 1) % len(circular_list)]])

    # Return the list of sublists

    return sublists
