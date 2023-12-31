
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 39th number
    fibonacci_sequence = [0, 1]
    for i in range(2, 39):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 39th Fibonacci number
    return decimal_integer % fibonacci_sequence[38] == 0
