
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = [list[i]]
        j = i + 1
        while j < len(list) and product * list[j] != -82:
            product *= list[j]
            sublist.append(list[j])
            j += 1
        if product == -82:
            result.append(sublist)
    return result
