
def prime_factors(numbers):
    return set(filter(lambda x: x in numbers, range(2, 61)))
