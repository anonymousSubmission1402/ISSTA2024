
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        product = 1
        sublist = []
        for j in range(i, len(my_list)):
            product *= my_list[j]
            if product == 93:
                result.append(sublist)
            elif product > 93:
                break
            else:
                sublist.append(my_list[j])
    return result
