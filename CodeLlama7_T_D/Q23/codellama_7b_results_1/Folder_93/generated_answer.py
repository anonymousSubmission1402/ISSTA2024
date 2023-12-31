
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all positive integers between 48 and 92, both inclusive
    for i in range(48, 93):

        # Check if 'i' is a divisor of 'n'
        if n % i == 0:

            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors
    return divisors
