
def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(1, x+1):
        if is_prime(i) and not str(i).startswith('0'):
            prime_list.append(i)
    
    left_truncatable_prime_list = []
    for i in prime_list:
        if is_left_right_truncatable_prime(i):
            left_truncatable_prime_list.append(i)
    
    return sorted(left_truncatable_prime_list)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    while len(str(n)) > 1:
        if not is_prime(n):
            return False
        n = int(str(n)[1:-1])
    return is_prime(n)
