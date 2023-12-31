
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 114th number in the Fibonacci sequence
    fib_114 = 0
    for i in range(113):
        fib_114 += fib[i]
        
    # Check if the decimal is divisible by the 114th number
    return decimal % fib_114 == 0
