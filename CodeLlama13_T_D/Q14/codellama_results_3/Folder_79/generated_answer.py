
def find_second_smallest_num(my_list):
    second_smallest = None
    for i in range(1, 5+1):
        if my_list[i] < my_list[1]:
            second_smallest = my_list[i]
    return second_smallest
