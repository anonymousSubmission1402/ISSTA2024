
def find_n_th_smallest_num(my_list):
    n = 8
    start = 11
    end = 52
    return sorted(my_list)[start:end][n-1]
