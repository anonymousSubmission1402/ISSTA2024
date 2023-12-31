
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal = int(binary_string, 2)

    # Compute the Fibonacci sequence up to 28
    fib = [0] + [1] + [sum(fib[i-1:i+1]) for i in range(2, 29)]

    # Check if the decimal is divisible by any of the numbers in the Fibonacci sequence up to 28
    return any(decimal % fib[i] == 0 for i in range(len(fib)))
