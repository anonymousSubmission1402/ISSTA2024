
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the current element and its predecessor
        product = 1

        # Initialize a variable to store the size of the current sublist
        size = 0

        # Iterate over the elements of the circular list starting from the current element
        for j in range(i, len(circular_list)):

            # Calculate the product of the current element and its predecessor
            product *= circular_list[j]

            # If the product is equal to -10, add the sublist to the list of sublists and break out of the loop
            if product == -10:
                sublists.append(circular_list[i:j+1])
                break

            # Increment the size of the current sublist
            size += 1

    # Return the list of sublists
    return sublists
