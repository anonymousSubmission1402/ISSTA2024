
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Initialize a variable to store the size of the current sublist
        size = 0

        # Iterate over the elements of the circular list starting from the current element
        for j in range(i, len(circular_list)):

            # Multiply the current element by the product of the previous elements
            product *= circular_list[j]

            # Increment the size of the current sublist
            size += 1

            # If the product equals -56, add the current sublist to the list of sublists
            if product == -56:
                sublists.append(circular_list[i:j+1])

            # If the size of the current sublist is greater than or equal to the size of the given list, break the loop
            if size >= len(circular_list):
                break

    # Return the list of sublists
    return sublists
