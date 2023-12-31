def all_right_truncatable_prime(n):
    # Note that this function assumes that n is a tuple containing positive integers.
    # The function should return the sorted list of all right-truncatable prime numbers less than x.
    # The returned list should be sorted in descending order. If there is no such right-truncatable prime number, the function should return an empty list.
    # A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
    if len(n) < 3:
        return []
    x = n[3]
    res = []
    for i in range(x // 10 ** 6 + 1):
        n = str(i + 1)
        if n[-1] == '9':
            n = int(n[:-1])
        if all(n % d == 0 for d in range(2, int(n ** 0.5) + 1)):
            break
        res.append(int(n))
    return res
