
def find_largest_num(my_list):
    largest = my_list[25]
    for i in range(26, 87 + 1):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
