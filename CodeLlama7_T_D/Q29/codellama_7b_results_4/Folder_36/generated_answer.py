
def gcf_two_nums(my_list):
    # Get the greatest common factor of two numbers
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Calculate the greatest common factor of the two specified indices
    return gcf(my_list[429], my_list[289])
