
def if_perfect_num(my_list):
    # Check if the list has at least 127 elements
    if len(my_list) < 127:
        return False

    # Get the integer at index 126
    num = my_list[126]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # If it's not a perfect number, return false
            return False

    # If we reach this point, the integer is a perfect number
    return True
