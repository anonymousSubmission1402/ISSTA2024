
def find_divisors_in_range(n):
    divisors = []
    for i in range(1, 10):
        if n % i == 0 and i <= n:
            divisors.append(i)
    return divisors
