
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b

    decimal_number = int(binary_string, 2)
    fibonacci_number = fibonacci(127)

    return decimal_number % fibonacci_number == 0
