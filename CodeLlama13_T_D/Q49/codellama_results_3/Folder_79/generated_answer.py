
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 13th number that occurs in the Fibonacci sequence
    fibonacci_number = 0
    for i in range(13):
        fibonacci_number += 5**i
    
    # Check if the decimal is divisible by the Fibonacci number
    return (decimal % fibonacci_number) == 0
