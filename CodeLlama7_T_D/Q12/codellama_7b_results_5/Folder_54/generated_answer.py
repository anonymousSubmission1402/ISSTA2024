
def find_smallest_num(numbers):
    smallest = None

    for i in range(74, 96):
        if smallest is None or numbers[i] < smallest:
            smallest = numbers[i]

    return smallest
