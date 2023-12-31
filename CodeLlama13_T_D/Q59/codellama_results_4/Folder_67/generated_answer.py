
def all_left_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            primes.append(number)
    return sorted(primes, reverse=True)

def is_left_truncatable_prime(number):
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
