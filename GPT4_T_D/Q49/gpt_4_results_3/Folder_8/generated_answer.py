
def if_decimal_is_divisible(bin_number):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_number = int(bin_number, 2)
    fibonacci_number = fibonacci(54)

    return decimal_number % fibonacci_number == 0
