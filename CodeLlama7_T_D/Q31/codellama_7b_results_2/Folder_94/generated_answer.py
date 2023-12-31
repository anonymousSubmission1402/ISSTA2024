
def if_perfect_num(my_list):
    if len(my_list) < 93:
        return False

    perfect_number = my_list[93]
    factors = []

    for i in range(1, int(perfect_number ** 0.5) + 1):
        if perfect_number % i == 0:
            factors.append(i)
            factors.append(perfect_number // i)

    if len(factors) == perfect_number - 1:
        return True

    else:

        return False
