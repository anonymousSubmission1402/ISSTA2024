
def if_perfect_num(my_list):
    if len(my_list) <= 410:
        return False

    perfect_number = my_list[410]

    if perfect_number < 0:

        return False


    divisors = []

    for i in range(1, int(perfect_number ** 0.5) + 1):

        if perfect_number % i == 0:

            divisors.append(i)

    if len(divisors) < 2:

        return False


    if sum(divisors) == perfect_number:

        return True


    else:


        return False
