
def find_n_th_smallest_num(my_list):
    # sort the list in ascending order
    my_list.sort()
    # return the 10th smallest number from index 260 to index 822, both inclusive
    return my_list[260:823].sort()[10]
