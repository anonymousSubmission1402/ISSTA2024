
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 31 <= i <= 72 and x > 1}
