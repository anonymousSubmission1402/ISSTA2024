
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to an integer
    decimal_integer = int(binary_representation, 2)
    # Find the seventh number that occurs in the Fibonacci sequence
    seventh_fibonacci_number = fibonacci(6)
    # Check if the decimal integer is divisible by the seventh Fibonacci number
    return (decimal_integer % seventh_fibonacci_number == 0)
def fibonacci(n):
    if n <= 1:
        return 1

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)
