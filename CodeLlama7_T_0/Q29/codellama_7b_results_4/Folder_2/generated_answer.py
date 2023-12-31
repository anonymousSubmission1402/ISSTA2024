
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # least common multiple until they
    # are equal.

    num1 = my_list[372]
    num2 = my_list[752]

    if num1 > num2:
        num1, num2 = num2, num1

    while num1 != num2:
        if num1 < num2:
            num2 -= num1
        else:
            num1 -= num2

    return num1
