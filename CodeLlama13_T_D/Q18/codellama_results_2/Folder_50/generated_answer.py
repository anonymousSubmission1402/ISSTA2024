
def sum_ints_div_by_either_nums(lst):
    start = 46
    end = 91
    divisors = [67, 15]
    return sum(x for x in lst[start:end+1] if x % divisors[0] == 0 or x % divisors[1] == 0)
