
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(461, 828):
        if n % i == 0 and i <= 827:
            result += i
    return result
