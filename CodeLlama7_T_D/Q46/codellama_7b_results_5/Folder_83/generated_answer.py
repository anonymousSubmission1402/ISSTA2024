
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers
    num1 = my_list[56]
    num2 = my_list[54]
    num3 = my_list[13]
    gcf = 1

    while True:
        if (num1 % gcf == 0) and (num2 % gcf == 0) and (num3 % gcf == 0):
            break

        else:
            gcf += 1

    return gcf
