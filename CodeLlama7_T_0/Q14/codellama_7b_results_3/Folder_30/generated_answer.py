
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize a variable to keep track of the second smallest element
    second_smallest = None

    # Iterate through the list starting from index 26 to index 52, both inclusive
    for i in range(26, 53):
        # If the current element is smaller than the second smallest element or if the second smallest element is None, update the second smallest element
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
