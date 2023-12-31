
def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = min(my_list)

    # Find the second smallest element in the list
    # by iterating through the list and comparing each element to the current smallest element
    second_smallest = None
    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        if (second_smallest is None) or (my_list[i] < second_smallest):
            second_smallest = my_list[i]
    return second_smallest
