
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fib = [0, 1]
    # Calculate the subsequent numbers in the Fibonacci sequence
    for i in range(2, len(fib)):
        fib.append(fib[i - 1] + fib[i - 2])
    # Check if the decimal integer is divisible by the 105th number in the Fibonacci sequence
    return decimal_int % fib[-1] == 0
