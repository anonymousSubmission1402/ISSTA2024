
def lists_with_product_equal_n(circular_list):
    # Find the product of all elements in the list
    product = 1
    for element in circular_list:
        product *= element

    # Initialize an empty list to store the sublists

    sublists = []

    # Iterate over the elements in the list

    for i in range(len(circular_list)):

        # If the product of the current sublist equals -65, add it to the list of sublists

        if product == -65:
            sublists.append(circular_list[i:] + circular_list[:i])

            # Break out of the loop once a sublist has been found

            break


        # Multiply the current element by the product of all previous elements

        product *= circular_list[i]


    return sublists
