
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal = int(binary_string, 2)
    
    # Compute the 166th number in the Fibonacci sequence
    fib166 = (1 + 5**0.5) ** 3 / 5
    
    # Return true if the decimal is divisible by the 166th Fibonacci number, else false
    return decimal % int(fib166) == 0
