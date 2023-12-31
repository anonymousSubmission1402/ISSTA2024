
def gcf_two_nums(my_list):
    # Get the greatest common factor of the two numbers
    gcf = None

    for i in range(1, min(my_list[46], my_list[84]) + 1):
        if my_list[46] % i == 0 and my_list[84] % i == 0:
            gcf = i

    return gcf
