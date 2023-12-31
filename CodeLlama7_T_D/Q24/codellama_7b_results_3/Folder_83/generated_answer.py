
def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):

        if n % i == 0:

            divisors.append(i)

    divisors = [d for d in divisors if 5 <= d and d <= 7]

    return sum(divisors)
