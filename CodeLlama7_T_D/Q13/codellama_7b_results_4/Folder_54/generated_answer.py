
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    sorted_list = sorted(my_list)

    for i in range(34, 56):
        if sorted_list[i] == sorted_list[-1]:
            continue

        else:

            return sorted_list[i]

    return None
