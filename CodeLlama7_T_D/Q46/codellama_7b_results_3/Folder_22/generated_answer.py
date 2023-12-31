
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 27, 85 and 51
    i = 27
    while i < len(my_list) - 2:
        if my_list[i] > my_list[i + 1]:
            gcf = my_list[i]
            while gcf * (i + 1) <= my_list[i + 2]:
                gcf += 1
            i += 1
        else:
            i += 1

    return gcf
