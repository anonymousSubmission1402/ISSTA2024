
def if_perfect_num(numbers):
    return numbers[94] == sum(divisors(numbers[94]))

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
