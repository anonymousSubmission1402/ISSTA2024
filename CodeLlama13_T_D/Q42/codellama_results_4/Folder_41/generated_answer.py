
def prime_factors(numbers):
    return set(factor for factor in range(2, numbers[84]) if numbers[84] % factor == 0 and all(number % factor != 0 for number in numbers))
