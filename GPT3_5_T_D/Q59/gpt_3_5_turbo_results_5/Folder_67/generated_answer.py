
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[71]
    primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncatable = True
        s = str(i)
        while s:
            if not is_prime(int(s)):
                truncatable = False
                break
            s = s[1:]
        if truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)
