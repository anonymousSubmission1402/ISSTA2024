
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    # at indices 33 and 72 in the list
    num1 = my_list[33]
    num2 = my_list[72]
    if num1 > num2:
        smaller_num = num2

    else:

        smaller_num = num1

    for i in range(2, smaller_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
