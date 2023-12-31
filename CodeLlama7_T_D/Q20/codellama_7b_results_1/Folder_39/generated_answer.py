
def find_n_th_smallest_num(my_list):
    # Initialize variables
    n = 7
    start_index = 47
    end_index = 89
    smallest_num = None

    # Loop through the list and find the nth smallest number
    for i in range(start_index, end_index + 1):
        if smallest_num == None or my_list[i] < smallest_num:
            smallest_num = my_list[i]
            if n == 0:
                break

            n -= 1

    return smallest_num
