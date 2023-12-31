
def composite_nums_between_indices(num_list):
    return {num for i, num in enumerate(num_list) if 36 <= i <= 46 and not is_prime(num)}

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
