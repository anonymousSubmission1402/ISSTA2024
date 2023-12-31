
def if_decimal_is_divisible(binary):
    # Convert the binary string to an integer
    num = int(binary, 2)
    
    # Compute the Fibonacci sequence up to the 16th number
    fib = [0] + [a + b for a, b in zip([0] + fib, fib)]
    
    # Check if the decimal integer corresponding to the given string is divisible by the 16th number that occurs in the Fibonacci sequence
    return num % fib[15] == 0
