
def find_smallest_num(my_list):
    smallest = my_list[639]
    for i in range(640, 976):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
