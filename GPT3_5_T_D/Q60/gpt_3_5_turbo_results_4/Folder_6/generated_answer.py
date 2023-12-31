
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        digits = str(n)
        for i in range(len(digits)):
            if not is_prime(int(digits[i:])):
                return False
            if not is_prime(int(digits[:i+1])):
                return False
        return True
    
    x = numbers[74]
    truncatable_primes = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
