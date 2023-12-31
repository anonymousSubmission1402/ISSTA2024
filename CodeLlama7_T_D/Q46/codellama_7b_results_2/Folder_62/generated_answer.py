
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers at a given index in a list
    def gcf(a, b):
        # Calculate the greatest common divisor of two positive integers
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    gcfs = []
    for i in range(10, 37):
        gcfs.append(gcf(my_list[i], my_list[i+1], my_list[i+2])))
    return max(gcfs)
