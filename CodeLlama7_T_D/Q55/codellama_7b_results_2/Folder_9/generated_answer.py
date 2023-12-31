
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the sublist
        product = 1

        # Loop through each element in the circular list starting from the current index
        for j in range(i, len(circular_list)):
            # Multiply the current element by the product variable
            product *= circular_list[j]

            # Check if the product is equal to -36
            if product == -36:
                # Append the sublist to the list of sublists
                sublists.append(circular_list[i:j+1])

    # Return the list of sublists
    return sublists
