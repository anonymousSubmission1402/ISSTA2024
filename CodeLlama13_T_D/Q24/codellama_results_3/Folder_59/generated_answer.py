
def sum_of_divisors_in_range(n):
    return sum([x for x in range(3, 6) if n % x == 0]) or 0
