
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 13, 76 and 44
    gcf = my_list[13]
    for i in range(14, 76):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
