
def all_odd_ints_exclusive(my_list):
    odds = []
    for i in range(50, 93):
        if my_list[i] % 2 != 0:
            odds.append(my_list[i])
    return odds
