
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0] + [1, 1]
    for i in range(3, len(fibonacci)):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    if decimal % fibonacci[90] == 0:
        return True
    else:
        return False
