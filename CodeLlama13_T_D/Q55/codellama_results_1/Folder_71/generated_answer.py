
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:i+1]
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == 47:
                result.append(sublist)
                break
            elif product > 47:
                break
    return result
