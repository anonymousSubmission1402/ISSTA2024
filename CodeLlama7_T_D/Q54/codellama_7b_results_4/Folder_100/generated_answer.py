
def all_right_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[26]
    prime_numbers = []

    # Check if the number is a right-truncatable prime number
    def check_right_truncatable_prime(number):
        # Check if the number is a prime number
        if not is_prime(number):
            return False

        # Check if the number remains prime when the last rightmost digit is successively removed
        for i in range(len(str(number)) - 1, 0, -1):
            if not is_prime(int(str(number)[:i] + str(number)[i+1:])):
                return False

        # If the number is a right-truncatable prime number, return True
        return True


    # Iterate through all numbers less than x and check if they are right-truncatable prime numbers
    for i in range(2, x):
        if check_right_truncatable_prime(i):
            prime_numbers.append(i)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers)


def is_prime(number):

    # Check if the number is greater than 1
    if number <= 1:
        return False

    # Check if the number is divisible by 2 to (number - 1)
    for i in range(2, number):
        if number % i == 0:
            return False

    # If the number is not divisible by any other number than itself and 1, it is prime
    return True
