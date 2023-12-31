
def prime_factors(my_list):
    # Check if input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers.")
    # Find the prime factors of the integer at index 15
    prime_factors = set()
    for i in range(15):
        if my_list[i] == 1:
            continue

        for j in range(i + 1, len(my_list)):
            if my_list[j] % my_list[i] == 0:
                prime_factors.add(my_list[i])
                break

    return prime_factors
