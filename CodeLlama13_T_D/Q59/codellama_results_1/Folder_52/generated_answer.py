
def all_left_truncatable_prime(numbers):
    x = numbers[52]
    result = []
    for i in range(1, x+1):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(n):
    if n < 2 or not str(n).isdigit():
        return False
    for i in range(1, int(len(str(n))/2)+1):
        if not is_prime(n):
            return False
        n = int(str(n)[i:])
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
