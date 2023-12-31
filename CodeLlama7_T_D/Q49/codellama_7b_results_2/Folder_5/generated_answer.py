
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to an integer
    num = int(binary_rep, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1

    # Loop through the numbers in the Fibonacci sequence until we find the 85th number
    while len(str(a + b)) != 85:
        a, b = b, a + b

    # Check if the decimal integer is divisible by the 85th number in the Fibonacci sequence
    return num % (a + b) == 0
