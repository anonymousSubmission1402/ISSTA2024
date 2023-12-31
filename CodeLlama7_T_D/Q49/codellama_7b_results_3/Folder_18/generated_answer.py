
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 199th Fibonacci number
    fibonacci_sequence = [0, 1]
    for i in range(2, 200):
        fibonacci_sequence.append(fibonacci_sequence[i - 2] + fibonacci_sequence[i - 1])
    # Check if the decimal integer is divisible by the 199th Fibonacci number
    return decimal_integer % fibonacci_sequence[198] == 0
