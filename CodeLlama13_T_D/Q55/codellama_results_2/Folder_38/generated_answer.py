
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        prod = 1
        sublist = [my_list[i]]
        for j in range(i+1, len(my_list)):
            prod *= my_list[j]
            if prod == -23:
                result.append(sublist)
                break
            elif prod > -23:
                break
            else:
                sublist.append(my_list[j])
    return result
