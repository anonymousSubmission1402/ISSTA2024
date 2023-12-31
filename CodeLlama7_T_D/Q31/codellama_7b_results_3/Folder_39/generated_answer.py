
def if_perfect_num(my_list):
    # Check if the list has at least 60 elements
    if len(my_list) < 60:
        return False

    # Calculate the sum of the factors of the number at index 59
    factor_sum = 1

    for i in range(2, int(my_list[59] ** 0.5) + 1):
        if my_list[59] % i == 0:
            factor_sum += i

    # Return true if the sum of the factors is equal to the number at index 59, otherwise return false
    return factor_sum == my_list[59]
