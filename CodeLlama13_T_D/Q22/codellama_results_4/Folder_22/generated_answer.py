
def find_sum_of_multiples(integer):
    sum = 0
    for i in range(1, 48):
        if i % integer == 0:
            sum += i
    return sum
