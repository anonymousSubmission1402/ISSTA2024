
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 187th Fibonacci number
    fibonacci_number = 0
    for i in range(187):
        fibonacci_number = fibonacci_number + (i + 1)
    # Check if the decimal integer is divisible by the Fibonacci number
    if (decimal_integer % fibonacci_number) == 0:
        return True

    else:

        return False
