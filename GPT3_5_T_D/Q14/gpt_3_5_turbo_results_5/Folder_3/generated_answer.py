
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers[27:56])
    if len(sorted_numbers) >= 2:
        return sorted_numbers[1]
    else:
        return None
