
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 2:
            if not is_prime(int(str(n)[1:-1])):
                return False
            n = int(str(n)[:-1])
        return is_prime(n) and is_prime(int(str(n)[0]))

    x = nums[992]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return left_right_truncatable_primes
