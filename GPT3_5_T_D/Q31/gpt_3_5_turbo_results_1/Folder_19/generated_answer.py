
def if_perfect_num(numbers):
    def is_perfect(n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return n == sum(divisors)

    if len(numbers) > 13 and is_perfect(numbers[13]):
        return True
    return False
