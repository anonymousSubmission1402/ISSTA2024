
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(51, 87):
        if lst[i] > 1:
            composites.add(lst[i])
    return composites
