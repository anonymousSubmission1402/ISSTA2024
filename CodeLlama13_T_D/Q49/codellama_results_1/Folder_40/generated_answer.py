
def if_decimal_is_divisible(binary_repr: str) -> bool:
    decimal = int(binary_repr, 2)
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
    return decimal % fibonacci[4] == 0
