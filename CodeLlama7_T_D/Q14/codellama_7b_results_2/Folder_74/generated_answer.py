
def find_second_smallest_num(my_list):
    if len(my_list) < 36 or len(my_list) > 46:
        return None

    else:

        second_smallest = None

        for i in range(35, 47):

            if my_list[i] < second_smallest or second_smallest is None:
                second_smallest = my_list[i]

        return second_smallest
