
def all_left_truncatable_prime(tuple):
    x = tuple[37]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False

    while len(str(n)) > 1:
        n = int(str(n)[:-1])

        if not is_prime(n):
            return False

    return True
