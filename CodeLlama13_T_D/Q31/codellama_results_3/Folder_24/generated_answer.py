
def if_perfect_num(arr):
    if len(arr) <= 74:
        return False
    else:
        num = arr[74]
        divisors = []
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                if num / i != i:
                    divisors.append(num // i)
        return sum(divisors) == num
