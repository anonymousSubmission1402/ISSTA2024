 def all_right_truncatable_prime(tuple):
    x = tuple[69]
    right_truncatable_prime_numbers = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i, x):
            right_truncatable_prime_numbers.append(i)
    return sorted(right_truncatable_prime_numbers, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n, x):
    last_digit = str(n)[-1]
    while int(last_digit) != 0 and int(last_digit) < x:
        n //= 10
        last_digit = str(n)[-1]
    if int(last_digit) == 0 or int(last_digit) >= x:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
