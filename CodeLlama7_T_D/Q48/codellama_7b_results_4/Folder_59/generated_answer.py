
def return_binary_or_hexa(tuple):
    a = tuple[0]
    b = tuple[10]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple:
            sum += i

    if sum % 2 == 1:
        return "{}".format(sum)

    else:

        hex_str = "{:x}".format(sum)

        return hex_str.strip("0")
