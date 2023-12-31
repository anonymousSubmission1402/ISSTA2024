
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Add the current element to the product
        product *= circular_list[i]

        # Check if the product is equal to 990
        if product == 990:
            # Initialize a list to store the elements in the current sublist
            sublist = []

            # Add the elements in the current sublist to the list
            for j in range(i, i + len(sublist)):
                sublist.append(circular_list[j])

            # Append the sublist to the list of sublists
            sublists.append(sublist)

    # Return the list of sublists
    return sublists
