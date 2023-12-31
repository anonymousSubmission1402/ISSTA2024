
def prime_factors(my_list):
    # Find the prime factorization of the number at index 84
    num = my_list[84]
    factors = []

    # Check if the number is divisible by any prime numbers less than its square root
    for i in range(int(num ** 0.5)):
        if num % i == 0:
            factors.append(i)
            factors.extend(prime_factors(my_list))
    return set(factors)
