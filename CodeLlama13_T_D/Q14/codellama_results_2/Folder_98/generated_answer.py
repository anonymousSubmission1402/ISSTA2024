
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(6, 7):
        if numbers[i] < numbers[5]:
            second_smallest = numbers[i]
    return second_smallest
