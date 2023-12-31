
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime or not
    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
    # Create an empty list to store the prime numbers
    primes = []
    # Iterate through the list and check if each number is prime using the lambda function
    for i in my_list:
        if is_prime(i):
            primes.append(i)
    # Sort the list of prime numbers in descending order
    primes.sort(reverse=True)
    return primes
