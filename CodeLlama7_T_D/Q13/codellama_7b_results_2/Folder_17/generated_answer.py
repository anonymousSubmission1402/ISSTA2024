 def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list has at least two elements

    if len(my_list) < 2:
        return None

    # Find the second largest element in the list

    sorted_list = sorted(my_list)
    second_largest = None
    for i in range(62, 79):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element or 'None' if it doesn't exist

    return second_largest
