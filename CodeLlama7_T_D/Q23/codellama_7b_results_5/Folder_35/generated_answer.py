
def find_divisors_in_range(n):
    # Initialize a list to store the divisors
    divisors = []

    # Loop through all the numbers between 392 and 465
    for i in range(392, 466):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors
    return divisors
