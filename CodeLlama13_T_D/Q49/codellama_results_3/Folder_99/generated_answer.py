
def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, num + 1):
        fibonacci_seq.append((fibonacci_seq[i - 1] + fibonacci_seq[i - 2]) % (10 ** 9 + 7))
    return fibonacci_seq[108] == 0
