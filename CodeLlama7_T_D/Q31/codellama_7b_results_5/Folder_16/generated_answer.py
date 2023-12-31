
def if_perfect_num(my_list):
    # Check if the list has at least 163 elements
    if len(my_list) < 163:
        return False

    # Calculate the sum of the divisors of the number at index 162
    sum_of_divisors = 0
    for i in range(1, int(my_list[162])**0.5 + 1):
        if my_list[162] % i == 0:
            sum_of_divisors += i + my_list[162]/i

    # Check if the sum of the divisors is equal to the number at index 162
    if sum_of_divisors == my_list[162]:
        return True

    else:

        return False
