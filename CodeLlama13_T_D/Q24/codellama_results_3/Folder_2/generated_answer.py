
def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(315, 956):
        if n % i == 0 and i >= 315 and i <= 955:
            sum += i
    return sum
