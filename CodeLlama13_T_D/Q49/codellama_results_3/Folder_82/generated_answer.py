
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_sequence = [0] + [1, 1] + [fibonacci_sequence[i-1] + fibonacci_sequence[i-2] for i in range(2, 99)]
    return decimal % fibonacci_sequence[98] == 0
