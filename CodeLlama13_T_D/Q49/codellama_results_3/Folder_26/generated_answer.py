
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, 138):
        fib.append(fib[i-1] + fib[i-2])
    decimal = int(binary, 2)
    return decimal % fib[137] == 0
