 def find_sum_of_multiples(num):
    if num < 0:
        raise ValueError("The number must be a positive integer.")
    sum = 0
    for i in range(1, 22):
        sum += (i * num)
    return sum
