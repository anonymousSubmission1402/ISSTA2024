
def sum_of_divisors_in_range(n):
    if n < 403 or n > 514:
        return 0

    else:

        divisors = []

        for i in range(403, 515):
            if n % i == 0:
                divisors.append(i)

        return sum(divisors)
