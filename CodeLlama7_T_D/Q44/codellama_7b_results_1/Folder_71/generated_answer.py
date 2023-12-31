
def composite_nums_between_indices(my_list):
    # Create a set to store the composite numbers
    composite_nums = set()

    # Loop through the list from index 59 to index 97
    for i in range(59, 98):
        # Check if the current number is composite using the prime factorization method
        if is_composite(my_list[i]):
            # Add the current number to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 59 to index 97, both inclusive
    return composite_nums

# Function to check if a number is composite using the prime factorization method
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all the numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n without leaving a remainder
            if n % i == 0:
                # Return False if i is a factor of n
                return False

    # If the loop completes successfully, then n is prime and returns True
    return True
