
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with a product equal to 76
    for i in range(len(circular_list)):
        product = 1

        # Calculate the product of the contiguous integers starting from the current index
        for j in range(i, len(circular_list)):
            product *= circular_list[j]

            # If the product is equal to 76, add the sublist to the list of sublists and reset the product to 1
            if product == 76:
                sublists.append(circular_list[i:j+1])
                product = 1

    return sublists
