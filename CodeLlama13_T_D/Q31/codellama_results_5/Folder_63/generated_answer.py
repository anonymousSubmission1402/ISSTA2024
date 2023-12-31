
def if_perfect_num(list):
    return list[57] in get_perfect_numbers(list)

def get_perfect_numbers(list):
    perfect_numbers = []
    for num in list:
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

def is_perfect_number(n):
    return sum(get_divisors(n)) == n

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return sorted(divisors)
