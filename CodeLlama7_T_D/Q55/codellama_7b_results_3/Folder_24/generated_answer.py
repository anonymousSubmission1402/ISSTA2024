
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Initialize a variable to store the starting index of the current sublist
        start_index = i

        # Loop through the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):

            # Calculate the product of the elements in the current sublist
            product *= circular_list[j]

            # Check if the product equals -89
            if product == -89:

                # Add the current sublist to the list of sublists
                sublists.append(circular_list[start_index:j + 1])

                # Break out of the inner loop
                break

    # Return the list of sublists
    return sublists
