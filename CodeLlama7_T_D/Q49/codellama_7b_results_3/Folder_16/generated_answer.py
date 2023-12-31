
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 128th Fibonacci number
    fib_128 = calculate_fibonacci(128)
    # Check if the decimal integer is divisible by the 128th Fibonacci number
    return decimal_integer % fib_128 == 0
def calculate_fibonacci(n):
    if n <= 1:
        return n

    else:

        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
