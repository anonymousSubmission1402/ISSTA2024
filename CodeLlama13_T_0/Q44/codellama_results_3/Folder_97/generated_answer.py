
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 15 <= i <= 39 and number > 1}
