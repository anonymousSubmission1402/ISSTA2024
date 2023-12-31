
def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(56, 58):
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers, reverse=True)
```

<Write a function called 'is_prime' that takes one argument, an integer, and returns True if the integer is prime or False otherwise.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
