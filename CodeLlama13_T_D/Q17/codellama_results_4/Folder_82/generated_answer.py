
def all_ints_div_by_both_two_nums(arr):
    res = []
    for i in range(20, 201):
        if arr[i] % -20 == 0 and arr[i] % -200 == 0:
            res.append(arr[i])
    return res
