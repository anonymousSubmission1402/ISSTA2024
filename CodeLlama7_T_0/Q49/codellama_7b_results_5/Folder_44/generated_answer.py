
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 159th Fibonacci number
    fib_159 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 159th Fibonacci number
    return decimal_integer % fib_159 == 0
