
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the list starting from index 20
    for i in range(20, len(my_list)):
        # Check if the number is divisible by any of the previous prime numbers
        for j in range(i - 1, -1, -1):
            if my_list[i] % my_list[j] == 0:
                break

        # If the number is not divisible by any of the previous prime numbers, it is a prime number
        else:
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers
