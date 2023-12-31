
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 477, 696 and 663
    gcf = my_list[477]
    for i in range(478, 696 + 1):
        if my_list[i] % gcf == 0 and my_list[i + 1] % gcf == 0:
            gcf = gcf * (my_list[i] / gcf) * (my_list[i + 1] / gcf)
    return gcf
