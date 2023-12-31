
def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:] + s[:i])):
            return False
    return True
