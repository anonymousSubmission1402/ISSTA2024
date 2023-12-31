
def if_perfect_num(lst):
    # Check if the list is empty or has less than 64 elements
    if len(lst) < 64:
        return False

    # Calculate the sum of the divisors of the number at index 64
    num = lst[64]
    sum_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i + num // i

    # Check if the sum of the divisors is equal to the number at index 64
    return sum_divisors == num
