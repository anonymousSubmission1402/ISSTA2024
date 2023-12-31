
def all_left_right_truncatable_prime(nums):
    primes = []
    for n in nums:
        if is_prime(n) and is_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
            return False
    return True
