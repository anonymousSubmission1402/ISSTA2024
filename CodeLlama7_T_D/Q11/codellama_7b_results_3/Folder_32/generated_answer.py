
def find_largest_num(numbers):
    largest = -float('inf')
    for i in range(21, 98):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
