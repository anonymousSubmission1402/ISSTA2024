
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = [lst[i]]
        for j in range(i+1, len(lst)):
            prod *= lst[j]
            if prod == 90:
                result.append(sublist + lst[j])
                break
        else:
            continue
    return result
