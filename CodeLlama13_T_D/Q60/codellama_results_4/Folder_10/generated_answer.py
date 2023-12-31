
def all_left_right_truncatable_prime(nums):
    x = nums[38]
    result = []
    for i in range(10, x+1):
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n < 10 or '0' in str(n):
        return False
    for i in range(len(str(n))-1, 0, -1):
        if not is_prime(int(str(n)[:i])):
            return False
    for j in range(2, len(str(n))):
        if not is_prime(int(str(n)[j:])):
            return False
    return True

def is_prime(n):
    if n < 2 or '0' in str(n):
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
