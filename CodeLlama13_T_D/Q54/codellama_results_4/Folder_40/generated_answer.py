
def all_right_truncatable_prime(nums):
    x = nums[10]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and is_rtp(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_rtp(n):
    while n > 10:
        last_digit = n % 10
        n //= 10
        if not is_prime(n*10+last_digit):
            return False
    return True
