
def all_left_right_truncatable_prime(x):
    # Initialize the list of left-and-right-truncatable prime numbers
    lst = []

    # Iterate from 1 to x

    for i in range(1, x + 1):

        # Check if i is a prime number

        if is_prime(i):

            # Check if the leading leftmost and last rightmost digits of i are both prime numbers

            if (is_prime(i // 10)) and (is_prime(i % 10))):

                # Add i to the list of left-and-right-truncatable prime numbers

                lst.append(i)

    # Sort the list of left-and-right-truncatable prime numbers in descending order

    lst = sorted(lst, reverse=True)

    return lst


def is_prime(n):

    # Check if n is an integer greater than 1

    if (n > 1) and (n % 2 != 0) or (n % 3 != 0)) and (n % 5 != 0)) and (n % 7 != 0))):

        # Check if n is not divisible by any integer between 2 and the square root of n

        for i in range(2, int(n ** 0.5) + 1)):

            if n % i == 0:

                return False

    return True
