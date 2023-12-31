
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 45th number that occurs in the Fibonacci sequence
    fibonacci_45 = 0
    for i in range(1, 46):
        if i == 45:
            break
        else:
            fibonacci_45 += (fibonacci[i] * fibonacci[i-1])
    
    # Check if the decimal integer is divisible by the 45th number that occurs in the Fibonacci sequence
    if decimal % fibonacci_45 == 0:
        return True
    else:
        return False
