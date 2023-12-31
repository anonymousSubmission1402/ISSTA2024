
import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    truncatable_primes = []
    
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable_prime = True
            temp = str(num)
            
            while len(temp) > 1:
                temp = temp[1:]
                
                if not is_prime(int(temp)):
                    is_truncatable_prime = False
                    break
            
            if is_truncatable_prime:
                truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
