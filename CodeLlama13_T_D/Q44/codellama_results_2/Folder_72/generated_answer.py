
def composite_nums_between_indices(numbers):
    return {n for i, n in enumerate(numbers) if 55 <= i <= 98 and n > 1}
