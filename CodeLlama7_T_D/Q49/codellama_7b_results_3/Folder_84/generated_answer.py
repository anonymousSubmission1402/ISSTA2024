
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence index
    fib_index = (decimal_integer - 1).bit_length() - 1
    # Check if the Fibonacci number at the given index is divisible by the decimal integer
    return (fib[fib_index] % decimal_integer) == 0
