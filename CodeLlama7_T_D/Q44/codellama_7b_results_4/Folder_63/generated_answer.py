
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is composite
        if my_list[i] > 1 and is_prime(my_list[i])):
            # If it is, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 17 to index 78, both inclusive
    return composite_nums

# Function to check if a number is prime or not
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is divisible by any number between 2 and n-1
        for i in range(2, n):
            if n % i == 0:
                return False

    # If we reach this point, then it means that n is a prime number
    return True
