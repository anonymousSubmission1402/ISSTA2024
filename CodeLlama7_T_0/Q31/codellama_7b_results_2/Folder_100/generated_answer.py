
def if_perfect_num(my_list):
    # Check if the list has at least 100 elements
    if len(my_list) < 100:
        return False

    # Get the integer at index 99
    num = my_list[99]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            while j != i:
                if j == num:
                    return True

                j += 1

    return False
