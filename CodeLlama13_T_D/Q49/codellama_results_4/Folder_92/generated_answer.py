
def if_decimal_is_divisible(binary_string):
    binary_int = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while True:
        next_fibonacci_number = fibonacci_sequence[-2] + fibonacci_sequence[-1]
        if next_fibonacci_number >= binary_int:
            break
        fibonacci_sequence.append(next_fibonacci_number)
    return (binary_int % fibonacci_sequence[6]) == 0
