
def sum_of_divisors_in_range(n):
    if n <= 57 or n >= 91:
        return 0
    
    divisors = []
    for i in range(58, 91):
        if i % n == 0:
            divisors.append(i)
            
    return sum(divisors)
