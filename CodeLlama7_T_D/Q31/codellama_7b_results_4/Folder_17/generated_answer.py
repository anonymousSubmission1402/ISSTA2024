
def if_perfect_num(lst):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in lst)):
        raise ValueError("Input must be a list of positive integers")
    # Check if the integer at index 632 is a perfect number
    if lst[632] == get_perfect_number(lst[632])):
        return True
    else:
        return False

def get_perfect_number(n):
    # Calculate the sum of the divisors of n
    sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if n / i != i:
                sum += n / i
    # Check if the sum of the divisors is equal to n
    if sum == n:
        return True
    else:
        return False
