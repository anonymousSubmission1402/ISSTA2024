
def find_second_largest_num(my_list):
    second_largest = None
    largest = my_list[42:68][0]
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
    return second_largest
