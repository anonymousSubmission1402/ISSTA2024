
def composite_nums_between_indices(numbers):
    indices = range(31, 72+1)
    composites = set()
    for i in indices:
        if numbers[i] > 1:
            composites.add(numbers[i])
    return composites
