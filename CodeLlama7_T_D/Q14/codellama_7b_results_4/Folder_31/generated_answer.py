
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize a variable to keep track of the second smallest element
    second_smallest = None

    # Iterate through the elements of the list
    for i in range(29, 94):
        # If the current element is smaller than the second smallest element, update the second smallest element
        if second_smallest is not None and my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
