
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(43, 52):
        if lst[i] > 1 and lst[i] not in composites:
            composites.add(lst[i])
    return composites
