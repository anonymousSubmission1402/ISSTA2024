
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    decimal_number = 0
    for i in range(len(binary_list)):
        decimal_number += (2 ** i) * binary_list[i]
    
    fibonacci_sequence = [0, 1]
    for i in range(56):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
        
    if decimal_number % fibonacci_sequence[56] == 0:
        return True
    else:
        return False
