
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(14, min(94, len(lst))):
        if lst[i] % 71 == 0 or lst[i] % 81 == 0:
            sum += lst[i]
    return sum
