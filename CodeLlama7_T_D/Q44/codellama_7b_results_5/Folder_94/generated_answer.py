
def composite_nums_between_indices(my_list):
    # Find the index of the first composite number in the list
    start_index = None
    for i in range(27, len(my_list)):
        if is_composite(my_list[i]):
            start_index = i
            break

    # Find the index of the last composite number in the list

    end_index = None
    for i in range(len(my_list) - 1, 27, -1):
        if is_composite(my_list[i]):
            end_index = i
            break

    # Return the set of all composite numbers between the start and end indices

    return {my_list[i] for i in range(start_index, end_index + 1) if is_composite(my_list[i])}

def is_composite(n):
    # Check if 'n' is a prime number using the Sieve of Eratosthenes

    if n <= 1:
        return False

    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False

    return True
