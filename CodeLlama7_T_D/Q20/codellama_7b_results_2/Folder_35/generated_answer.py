
def find_n_th_smallest_num(my_list):
    # sort the list in ascending order
    my_list.sort()
    # get the index of the 6th smallest number from index 12 to index 60, both inclusive
    nth_index = (12 + 60) // 2
    return my_list[nth_index]
