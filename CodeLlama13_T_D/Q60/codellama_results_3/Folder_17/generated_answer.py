
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if str(num).count("0") == 0 and is_prime(num) and all(is_prime(int(str(num)[1:]))) and all(is_prime(int(str(num)[:-1]))):
            result.append(num)
    return sorted(result, reverse=True)
