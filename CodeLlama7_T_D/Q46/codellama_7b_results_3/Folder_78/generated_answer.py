
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the three numbers
    gcf = my_list[13]
    for i in range(70, 32, -1):
        if my_list[i] < gcf:
            gcf = my_list[i]
    return gcf
