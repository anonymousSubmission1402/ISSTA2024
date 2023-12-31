
def sum_of_divisors_in_range(n):
    if n < 1:
        return 0

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)

    sum_of_divisors = 0

    for d in divisors:
        if 5 <= d <= 8:
            sum_of_divisors += d

    return sum_of_divisors
