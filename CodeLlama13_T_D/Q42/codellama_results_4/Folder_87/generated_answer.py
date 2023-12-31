
def prime_factors(numbers):
    # Calculate the set of all prime factors for each number in the list
    prime_factor_sets = [set(prime_factors(n)) for n in numbers]
    
    # Return the union of all prime factor sets
    return set.union(*prime_factor_sets)
