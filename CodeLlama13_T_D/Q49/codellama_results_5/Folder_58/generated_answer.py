
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, len(fib)):
        fib.append(fib[i-1] + fib[i-2])
    n = int(binary, 2)
    return n % fib[104] == 0
