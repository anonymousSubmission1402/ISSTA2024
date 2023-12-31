
def find_primes_between_indices(my_list):
    # Find the first prime number in the range
    first_prime = None
    for i in range(112, 361 + 1):
        if is_prime(i):
            first_prime = i
            break

    # Find all prime numbers between the indices

    primes = []

    for i in range(first_prime, 361 + 1):
        if is_prime(i):
            primes.append(i)

    return sorted(primes, reverse=True)

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True
