
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = sorted(numbers)[-2]
    return second_largest
