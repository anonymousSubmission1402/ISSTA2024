
def all_left_right_truncatable_prime(nums):
    return sorted([x for x in nums if is_left_right_truncatable_prime(x)], reverse=True)

def is_left_right_truncatable_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return all([is_prime(str(n)[i:]) and is_prime(str(n)[:len(str(n))-i]) for i in range(1, len(str(n)))])

def is_prime(s):
    if s == "0" or s == "1":
        return False
    for i in range(2, int(s**0.5)+1):
        if s % i == 0:
            return False
    return True
