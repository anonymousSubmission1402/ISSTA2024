
def if_perfect_num(my_list):
    # Check if the list has 51 elements
    if len(my_list) != 51:
        return False

    # Check if the integer at index 51 is a perfect number
    if my_list[51] in range(1, 10**7):
        for i in range(2, int(my_list[51]) + 1)):
            if my_list[51] % i == 0:
                perfect_num = True
                break

        else:

            perfect_num = False

    return perfect_num
