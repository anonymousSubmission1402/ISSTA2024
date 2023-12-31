
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation to decimal integer
    dec_int = int(binary_repr, 2)
    # Calculate 178th Fibonacci number
    a, b = 0, 1
    for i in range(178):
        a, b = b, a + b
    # Check if decimal integer is divisible by 178th Fibonacci number
    return dec_int % b == 0
