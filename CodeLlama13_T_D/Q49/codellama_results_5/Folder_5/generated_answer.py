
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Compute the Fibonacci sequence up to 85th number
    fib_seq = [0, 1]
    for i in range(83):
        fib_seq.append(fib_seq[i] + fib_seq[i+1])
    
    # Check if the decimal is divisible by any of the numbers in Fibonacci sequence
    for num in fib_seq:
        if decimal % num == 0:
            return True
    
    return False
