
def if_perfect_num(lst):
    return lst[849] == sum([i for i in range(1, int(lst[849])//2+1) if lst[849] % i == 0])
