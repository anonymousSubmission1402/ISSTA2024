
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = sorted(numbers)[1]
    for i in range(1, 9):
        if numbers[i] == second_largest:
            return second_largest
    return None
