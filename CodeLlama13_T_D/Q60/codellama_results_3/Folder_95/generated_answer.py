
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable_prime(n):
        if not str(n).startswith('0') and is_prime(n):
            for i in range(len(str(n)) - 1, 0, -1):
                if not is_prime(int(str(n)[:i])):
                    return False
        return True

    return sorted([x for x in numbers if truncatable_prime(x)])
