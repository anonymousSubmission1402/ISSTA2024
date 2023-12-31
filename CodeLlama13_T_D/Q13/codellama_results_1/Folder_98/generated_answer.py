
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    largest = my_list[0]
    second_largest = None
    for i in range(1, 7):
        num = my_list[i]
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest
