
def find_largest_num(my_list):
    largest = my_list[262]
    for i in range(263, 747):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
