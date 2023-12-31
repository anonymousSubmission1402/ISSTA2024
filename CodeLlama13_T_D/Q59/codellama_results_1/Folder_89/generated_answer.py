
def all_left_truncatable_prime(nums):
    x = nums[97]
    primes = []
    for i in range(x):
        if is_prime(i) and not has_zero(str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)
