
def find_primes_between_indices(lst):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    primes = [num for num in lst[20:49] if is_prime(num)]
    return sorted(primes, reverse=True)
