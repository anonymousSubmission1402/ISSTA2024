
def find_primes_between_indices(nums):
    primes = []
    for i in range(24, 33):
        if nums[i] % 2 == 0 and nums[i] % 3 == 0:
            primes.append(nums[i])
    return sorted(primes, reverse=True)
