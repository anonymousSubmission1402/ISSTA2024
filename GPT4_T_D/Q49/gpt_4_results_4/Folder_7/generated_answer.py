
def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    for i in range(2, 160):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal = int(binary_representation, 2)
    return decimal % fib[160 - 1] == 0
