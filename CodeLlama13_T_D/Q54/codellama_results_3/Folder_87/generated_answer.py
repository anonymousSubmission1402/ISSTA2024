
def all_right_truncatable_prime(numbers):
    prime_list = []
    for number in numbers:
        if is_right_truncatable_prime(number):
            prime_list.append(number)
    return sorted(prime_list, reverse=True)

def is_right_truncatable_prime(n):
    if n < 2 or not is_prime(n):
        return False
    for i in range(1, int(math.log10(n)) + 1):
        if not is_prime(n // (10 ** i)):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
