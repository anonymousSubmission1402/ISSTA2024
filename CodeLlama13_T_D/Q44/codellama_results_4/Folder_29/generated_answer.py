
def composite_nums_between_indices(numbers):
    composites = []
    for i in range(52, 72):
        if numbers[i] > 1:
            composites.append(numbers[i])
    return set(composites)
