
def composite_nums_between_indices(my_list):
    indices = {i for i in range(52, 71+1)}
    return set(filter(lambda x: x > 1 and x % 10 == 0, my_list)) & indices
