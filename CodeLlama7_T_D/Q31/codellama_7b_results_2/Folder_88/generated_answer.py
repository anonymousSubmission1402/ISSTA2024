
def if_perfect_num(lst):
    if len(lst) < 47:
        return False

    num = lst[46]

    factors = []

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)

    return sum(factors) == num
