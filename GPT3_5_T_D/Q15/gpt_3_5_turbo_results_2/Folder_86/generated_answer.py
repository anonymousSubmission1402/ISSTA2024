
def sum_odd_ints_inclusive(lst):
    odd_ints = [num for num in lst[31:35] if num % 2 != 0]
    if len(odd_ints) == 0:
        return 0
    return sum(odd_ints)
