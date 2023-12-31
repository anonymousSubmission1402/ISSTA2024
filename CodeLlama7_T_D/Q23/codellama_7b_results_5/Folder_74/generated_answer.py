
def find_divisors_in_range(n):
    # create a list of all positive divisors of n
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
    # filter the list to only include divisors between 40 and 74
    filtered_divisors = [d for d in divisors if 40 <= d <= 74]
    return filtered_divisors
