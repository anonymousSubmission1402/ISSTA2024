
def find_n_th_smallest_num(my_list):
    # sort the list in ascending order
    my_list.sort()
    # return the 6th smallest number from index 40 to index 99, both inclusive
    return my_list[40:99+1].index(my_list[40+5]) + 40
