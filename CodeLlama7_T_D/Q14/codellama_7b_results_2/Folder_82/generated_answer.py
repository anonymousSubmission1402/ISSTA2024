
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")

    # Check if the list is empty

    if len(my_list) == 0:
        return None


    # Find the smallest element in the list

    smallest = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]


    # Find the second smallest element in the list

    second_smallest = None

    for i in range(len(my_list)):
        if my_list[i] > smallest and (second_smallest is None or my_list[i] < second_smallest):
            second_smallest = my_list[i]

    return second_smallest
