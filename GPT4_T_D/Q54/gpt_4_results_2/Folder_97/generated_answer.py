
def all_right_truncatable_prime(nums):
    from sympy import isprime
    
    def is_right_truncatable(n):
        while n != 0:
            if not isprime(n):
                return False
            n = n // 10
        return True

    x = nums[645]
    return sorted([i for i in range(2, x) if is_right_truncatable(i)])
