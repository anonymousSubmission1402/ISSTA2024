
def lists_with_product_equal_n(list, n):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = [list[i]]
        j = (i + 1) % len(list)
        while j != i and product < n:
            product *= list[j]
            sublist.append(list[j])
            j = (j + 1) % len(list)
        if product == n:
            result.append(sublist)
    return result
