
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 48th Fibonacci number
    fib_48 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 48th Fibonacci number
    return decimal_integer % fib_48 == 0
