
def sum_of_divisors_in_range(n):
    total = 0
    for i in range(3, n + 1):
        if n % i == 0 and i <= 5:
            total += i
    return total
