
def all_neg_ints_inclusive(lst):
    neg_ints = []
    for num in lst[0:10]:
        if num < 0:
            neg_ints.append(num)
    return neg_ints
