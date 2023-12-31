
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Compute the 6th Fibonacci number
    fibonacci_6 = (5 + sqrt(5)) / 2 # Golden ratio
    # Check if the decimal integer is divisible by the 6th Fibonacci number
    return decimal_integer % fibonacci_6 == 0
