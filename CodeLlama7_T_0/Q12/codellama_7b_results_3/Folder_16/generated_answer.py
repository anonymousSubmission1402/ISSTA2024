
def find_smallest_num(my_list):
    smallest = my_list[26]
    for i in range(27, 75):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
