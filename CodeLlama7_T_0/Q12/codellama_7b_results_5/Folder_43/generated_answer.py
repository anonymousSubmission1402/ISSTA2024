
def find_smallest_num(my_list):
    smallest = None

    for i in range(23, 24):
        if smallest is None or my_list[i] < smallest:
            smallest = my_list[i]

    return smallest
