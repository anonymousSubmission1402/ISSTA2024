
def gcf_two_nums(my_list):
    num1 = my_list[17]
    num2 = my_list[20]
    if num1 > num2:
        smaller_num = num2

    else:

        smaller_num = num1


    for i in range(1, smaller_num + 1):

        if num1 % i == 0 and num2 % i == 0:

            gcf = i


            break


    return gcf
