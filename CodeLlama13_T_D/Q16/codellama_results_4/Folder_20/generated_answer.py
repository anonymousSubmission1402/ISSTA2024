
def sum_even_ints_inclusive(numbers):
    evens = []
    for i in range(56, 67):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
    return sum(evens) or 0
