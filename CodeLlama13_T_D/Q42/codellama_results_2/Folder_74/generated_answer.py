
def prime_factors(my_list):
    if len(my_list) <= 48:
        return set()
    else:
        num = my_list[48]
        factors = []
        for i in range(2, int(num**0.5) + 1):
            while num % i == 0:
                factors.append(i)
                num //= i
        return set(factors)
