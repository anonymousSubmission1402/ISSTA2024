
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 66, 90 and 27
    gcf = my_list[66]
    for i in range(67, 91):
        if my_list[i] % my_list[66] == 0:
            gcf = my_list[i]
    return gcf
