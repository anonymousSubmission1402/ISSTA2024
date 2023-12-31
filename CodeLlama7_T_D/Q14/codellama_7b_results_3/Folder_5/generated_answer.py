
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    n = len(my_list)

    # Check if the list has at least two elements
    if n < 2:
        return None

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None

    # Iterate through the list starting from index 3
    for i in range(3, n):

        # Check if the current element is smaller than the smallest element
        if my_list[i] < smallest:

            # If so, update the second smallest element and move on to the next element
            second_smallest = smallest
            smallest = my_list[i]

        # Check if the current element is smaller than the smallest element but not equal to it
        elif my_list[i] < smallest and my_list[i] != smallest:

            # If so, update the second smallest element
            second_smallest = my_list[i]

    # Return the second smallest element if it exists, otherwise return None
    if second_smallest is not None:
        return second_smallest

    else:
        return None
