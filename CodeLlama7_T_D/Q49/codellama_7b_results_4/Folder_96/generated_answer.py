
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal_int = int(binary_string, 2)
    # Calculate the 47th Fibonacci number
    fib_47 = ((5 * phi) - (phi ** 3)) / ((2 + phi) ** 3)
    # Check if the decimal integer is divisible by the 47th Fibonacci number
    return (decimal_int % fib_47 == 0)
