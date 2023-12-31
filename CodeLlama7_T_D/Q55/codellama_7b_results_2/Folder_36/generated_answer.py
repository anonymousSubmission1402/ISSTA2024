
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find all contiguous sequences of integers whose product is equal to n

    for i in range(len(circular_list)):
        # Get the current element and its next element
        curr_elem = circular_list[i]
        next_elem = circular_list[(i + 1) % len(circular_list)]

        # Check if the product of the current element and its next element is equal to n
        if curr_elem * next_elem == n:
            # Get the sublist that starts with the current element and ends with its next element
            sublist = circular_list[i:]

            # Add the sublist to the list of sublists
            sublists.append(sublist)

    return sublists
