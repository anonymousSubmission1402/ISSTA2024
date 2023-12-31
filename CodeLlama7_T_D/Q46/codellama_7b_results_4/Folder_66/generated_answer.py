
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # using the Euclidean algorithm

    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = my_list[92]
    num2 = my_list[69]
    num3 = my_list[95]
    gcf12 = gcf(num1, num2)
    gcf123 = gcf(gcf12, num3)
    return gcf123
