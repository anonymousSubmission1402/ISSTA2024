
def if_decimal_is_divisible(binary):
    # Convert the binary string to an integer
    n = int(binary, 2)
    
    # Calculate the number that occurs in the Fibonacci sequence
    fib = [0, 1]
    for i in range(68):
        fib.append(fib[i-1] + fib[i])
        
    # Check if the number is divisible by the 68th Fibonacci number
    return n % fib[68] == 0
