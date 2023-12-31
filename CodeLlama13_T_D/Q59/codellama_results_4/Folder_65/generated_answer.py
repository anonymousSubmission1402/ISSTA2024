
def all_left_truncatable_prime(numbers):
    result = []
    for n in numbers:
        if is_left_truncatable_prime(n):
            result.append(n)
    return sorted(result)

def is_left_truncatable_prime(n):
    if n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(1, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True
