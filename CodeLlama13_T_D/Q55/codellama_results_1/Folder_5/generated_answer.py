
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = [list[i]]
        for j in range(i+1, len(list)):
            product *= list[j]
            if product == -33:
                result.append(sublist)
                break
            else:
                sublist.append(list[j])
    return result
