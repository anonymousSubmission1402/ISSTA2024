
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the remainder of dividing the integer by the 195th Fibonacci number
    fibonacci_194 = 377.0
    fibonacci_195 = 610.0
    remainder = decimal_int % (fibonacci_194 + fibonacci_195)
    # Return True if the remainder is zero, False otherwise
    return remainder == 0.0
