
def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        product = 1
        temp = lst[i:] + lst[:i]
        for j in range(len(temp)):
            product *= temp[j]
            if product == -5:
                sublists.append(temp[:j+1])
    return sublists
