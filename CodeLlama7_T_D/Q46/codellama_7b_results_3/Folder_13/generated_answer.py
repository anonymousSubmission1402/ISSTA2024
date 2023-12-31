
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the greatest common factor of the three numbers
    return gcf(gcf(my_list[991], my_list[244]), my_list[974])
