def return_binary_or_hexa(test_tup):
    res = test_tup[10] + 1
    end = test_tup[12] - 1
    if res <= end:
        res += test_tup[11] - test_tup[10]
        if res % 2 == 1:
            return bin(res)[2:]
        else:
            return hex(res)[2:]
    else:
        return ""
