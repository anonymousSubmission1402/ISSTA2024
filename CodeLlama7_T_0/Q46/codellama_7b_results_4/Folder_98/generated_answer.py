
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 8, 2 and 1
    gcf = my_list[8]
    for i in range(9, len(my_list)):
        if my_list[i] % gcf == 0:
            return gcf

    return 1
