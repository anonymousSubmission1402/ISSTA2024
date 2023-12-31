
def if_decimal_is_divisible(binary):
    # Convert the binary representation string to an integer
    decimal = int(binary, 2)
    
    # Calculate the 126th number that occurs in the Fibonacci sequence
    fibonacci = [0] * 126
    for i in range(126):
        if i == 0:
            fibonacci[i] = 0
        elif i == 1:
            fibonacci[i] = 1
        else:
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    divisor = fibonacci[125]
    
    # Check if the decimal integer is divisible by the divisor
    return (decimal % divisor) == 0
