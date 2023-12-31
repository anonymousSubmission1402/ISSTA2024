
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 1 to n-1 (exclude n)
    for i in range(1, n):

        # Check if i is a divisor of n
        if n % i == 0:

            # If the divisor is between 3 and 7, inclusive
            if 3 <= i <= 7:
                # Add the divisor to the list
                divisors.append(i)

    # Return the list of divisors
    return divisors
