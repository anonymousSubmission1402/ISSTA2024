
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    gcf = 1
    for i in range(2, min(my_list[0], my_list[9]) + 1)):
        if my_list[0] % i == 0 and my_list[9] % i == 0:
            gcf = i

    return gcf
