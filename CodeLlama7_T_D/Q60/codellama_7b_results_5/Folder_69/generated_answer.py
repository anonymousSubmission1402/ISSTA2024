
def all_left_right_truncatable_prime(tuple):
    x = tuple[760]
    prime_numbers = []

    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_right_truncatable_prime(n):

    if str(n)[0] == "0" or str(n)[-1] == "0":
        return False

    for i in range(len(str(n)))):
        if int(str(n))[:i] == 0 or int(str(n))[i:] == 0:
            return False

    return True
