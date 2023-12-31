
def if_perfect_num(my_list):
    # Check if the list has at least 223 elements
    if len(my_list) < 223:
        return False

    # Find the value of the number at index 222
    num = my_list[222]

    # Check if the number is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num:
                return True

    # If we reach this point, the number is not a perfect number
    return False
