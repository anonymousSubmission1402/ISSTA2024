
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the second largest element
    second_largest = None
    second_largest_index = -1

    # Iterate through the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element, or 'None' if there is no such element
    return second_largest if second_largest_index >= 527 and second_largest_index <= 538 else None
