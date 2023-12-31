
def gcf_three_nums(my_list):
    return __gcf(my_list[20], my_list[51], my_list[62])

def __gcf(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 0
    for i in range(min(a, b, c), max(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            return i
    return 1
