
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 20 <= i <= 30 and x > 1}
