def sum_of_divisors_in_range(n):
    if n < 15 or n > 92:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n == 3:
        return 6
    if n == 4:
        return 10
    if n == 5:
        return 15
    if n == 6:
        return 21
    if n == 7:
        return 28
    if n == 8:
        return 36
    if n == 9:
        return 45
    if n == 10:
        return 55
    if n == 11:
        return 66
    if n == 12:
        return 78
    if n == 13:
        return 91
    if n == 14:
        return 92
    return (sum_of_divisors_in_range(n - 1) + sum_of_divisors_in_range(n + 1)) - sum_of_divisors_in_range(n)
