
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the integers at indices 23 and 27
    gcf = 1
    for i in range(23, 28):
        if my_list[i] % gcf == 0:
            continue

        else:

            while my_list[i] % gcf != 0:
                gcf += 1

    return gcf
