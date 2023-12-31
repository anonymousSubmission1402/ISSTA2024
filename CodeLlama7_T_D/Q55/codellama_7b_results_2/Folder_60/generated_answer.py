
def lists_with_product_equal_n(circular_list):
    # Find the product of all elements in the list
    product = 1
    for element in circular_list:
        product *= element

    # If the product is not equal to 49, return an empty list
    if product != 49:
        return []

    # Initialize a list to store the sublists

    sublists = []

    # Iterate over the elements in the list

    for element in circular_list:

        # If the product of the current sublist is equal to 49, add it to the list of sublists and reset the sublist

        if product == 49:
            sublists.append(sublist)
            sublist = []

            # Reset the product to 1

            product = 1

        # Add the current element to the sublist

        sublist.append(element)

        # Update the product of the current sublist

        product *= element


    # If there are no sublists with a product equal to 49, return an empty list

    if not sublists:
        return []

    # Return the list of sublists with a product equal to 49

    return sublists
