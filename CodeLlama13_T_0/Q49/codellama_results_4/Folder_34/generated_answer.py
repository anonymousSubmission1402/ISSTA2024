
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 24th number in the Fibonacci sequence
    fib24 = (13*13 - 5*5)*(13*13 + 5*5)/(2*13*13 - 5*5)
    
    # Check if the decimal is divisible by the 24th number in the Fibonacci sequence
    return decimal % fib24 == 0
