def return_binary_or_hexa(test_tup):
    res = test_tup[55] + 1
    res += test_tup[84] - test_tup[55] - 1
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
