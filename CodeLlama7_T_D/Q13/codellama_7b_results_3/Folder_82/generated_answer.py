
def find_second_largest_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element
    second_largest = None
    current_index = 20

    # Iterate through the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] > my_list[current_index]:
            second_largest = my_list[i]
            current_index = i

    # Return the second largest element or None if it does not exist
    return second_largest
