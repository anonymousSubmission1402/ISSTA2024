
def find_largest_num(numbers):
    largest_element = None
    for i in range(62, 93):
        if largest_element is None or numbers[i] > largest_element:
            largest_element = numbers[i]
    return largest_element
