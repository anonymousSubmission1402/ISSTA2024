
def sum_of_divisors_in_range(n):
    return sum(d for d in range(46, 90) if n % d == 0) or 0
