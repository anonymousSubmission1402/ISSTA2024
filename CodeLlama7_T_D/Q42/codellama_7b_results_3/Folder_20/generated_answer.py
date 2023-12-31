
def prime_factors(my_list):
    # Get the integer at index 53
    num = my_list[53]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all numbers less than or equal to the sqrt of the input number
    for i in range(2, int(num ** 0.5) + 1):
        # If the current number is a factor of the input number, add it to the set of prime factors
        if num % i == 0:
            prime_factors.add(i)
    return prime_factors
