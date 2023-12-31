
def all_right_truncatable_prime(numbers):
    prime_list = []
    for num in numbers:
        if is_prime(num) and is_right_truncatable(num):
            prime_list.append(num)
    return sorted(prime_list)
```
This function takes a tuple of positive integers as input, and returns the sorted list of all right-truncatable prime numbers less than `x`. The function uses the `is_prime` and `is_right_truncatable` functions to check if a number is prime and whether it is a right-truncatable prime. If there are no such right-truncatable prime numbers, the function returns an empty list.

The `is_prime` function checks if a number is prime by checking if it is divisible by any number between 2 and the square root of the number.
```
def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
```
The `is_right_truncatable` function checks if a number is a right-truncatable prime by successively removing the last digit of the number and checking if it is still a prime. If the number becomes not prime, it means that it is no longer a right-truncatable prime.
```
def is_right_truncatable(num):
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True
