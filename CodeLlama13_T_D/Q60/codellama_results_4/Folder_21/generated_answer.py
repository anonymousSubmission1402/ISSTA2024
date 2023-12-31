
def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and no_zeroes(str(i)):
            prime_list.append(i)
    return prime_list

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def no_zeroes(s):
    return '0' not in s
