
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")

    # Check if the list contains at least one element

    if len(my_list) < 1:
        raise ValueError("List must contain at least one element")

    # Find the second largest element in the specified range

    second_largest = None

    for i in range(15, 39 + 1):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element

    return second_largest
