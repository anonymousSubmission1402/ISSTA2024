
def if_perfect_num(my_list):
    if len(my_list) < 48:
        return False

    i = 48

    while i > 1:

        if my_list[i] % my_list[i - 1] != 0:
            return False

        i -= 1

    return True
