
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = []
        for j in range(i, len(list)):
            product *= list[j]
            sublist.append(list[j])
            if product == -87:
                result.append(sublist)
    return result
