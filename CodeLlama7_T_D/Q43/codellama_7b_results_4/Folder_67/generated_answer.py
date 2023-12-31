
def find_primes_between_indices(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(i, int) for i in my_list)):
        raise ValueError("Input must be a list of integers")
    # Find prime numbers between indices 17 and 79 (inclusive)
    prime_numbers = []
    for i in range(17, 80):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers

def is_prime(n):

    # Check if n is less than 2

    if n < 2:

        return False

    # Check if n is divisible by 2 to n-1

    for i in range(2, n):

        if n % i == 0:

            return False

    return True
