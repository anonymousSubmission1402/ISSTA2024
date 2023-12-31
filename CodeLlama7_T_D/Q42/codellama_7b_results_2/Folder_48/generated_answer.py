
def prime_factors(numbers):
    # find the number at index 247 in the list
    target_number = numbers[247]
    # initialize an empty set to store the prime factors
    prime_factors = set()
    # loop through all the numbers in the list
    for num in numbers:
        # if the number is a factor of the target number and it is also a prime number
        if (num % target_number == 0) and (is_prime(num)):
            # add it to the set of prime factors
            prime_factors.add(num)
    return prime_factors

def is_prime(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    # check if n is divisible by 2 to n-1
    for i in range(2, n+1):
        if n % i == 0:
            return False

    return True
