
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for i in range(len(my_list)):
        product *= my_list[i]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through the list of integers and check if each integer is a factor of the product
    for i in range(len(my_list)):
        if product % my_list[i] == 0:
            # If the integer is a factor, add it to the set of prime factors
            prime_factors.add(my_list[i])
    return prime_factors
