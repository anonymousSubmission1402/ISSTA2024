
def all_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if is_prime(x) and is_right_truncatable_prime(x):
            primes.append(x)
    return sorted(primes, reverse=True)
```
This function takes a tuple of positive integers as input and returns a list of all right-truncatable prime numbers less than the integer at index 29 in the tuple. The returned list is sorted in descending order. If there are no such right-truncatable prime numbers, an empty list is returned.

The function uses two helper functions: `is_prime` and `is_right_truncatable_prime`. `is_prime` checks if a given number is a prime number or not, while `is_right_truncatable_prime` checks if a given number is a right-truncatable prime number.

Here is the code for these helper functions:
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True
