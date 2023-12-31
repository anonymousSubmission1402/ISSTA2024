
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 189):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return decimal % fibonacci[188] == 0
