
def all_left_truncatable_prime(x):
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
