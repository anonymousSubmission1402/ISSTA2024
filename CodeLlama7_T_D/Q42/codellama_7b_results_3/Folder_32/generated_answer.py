
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    total = 1
    for element in my_list:
        total *= element
    # Initialize an empty set to store the prime factors

    prime_factors = set()
    # Loop through all possible prime factors

    for i in range(2, int(total ** 0.5) + 1):
        # If the current number is a factor of the total product

        if total % i == 0:
            # Add it to the set of prime factors

            prime_factors.add(i)
    return prime_factors
