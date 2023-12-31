
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 34 is a perfect number
    if my_list[34] == 0 or my_list[34] % 2 != 0:
        return False

    # Calculate the sum of the divisors of the element at index 34
    sum_of_divisors = 1
    for i in range(2, int(my_list[34]) ** 0.5 + 1):
        if my_list[34] % i == 0:
            sum_of_divisors += i + my_list[34] / i

    # Check if the element at index 34 is a perfect number
    if sum_of_divisors == 2 * my_list[34]:
        return True

    else:

        return False
