
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 15, 51 and 76
    gcf = my_list[15]
    for i in range(16, 51):
        gcf = gcd(gcf, my_list[i])
    for i in range(52, 76):
        gcf = gcd(gcf, my_list[i])
    return gcf
