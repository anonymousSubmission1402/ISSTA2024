
def all_left_right_truncatable_prime(numbers):
    x = numbers[4]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_left_and_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] == '0':
            return False
        if not is_prime(int(s[:i+1])) or not is_prime(int(s[i+1:])):
            return False
    return True
