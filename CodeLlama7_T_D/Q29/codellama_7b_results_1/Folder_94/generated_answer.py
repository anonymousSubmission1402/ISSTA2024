
def gcf_two_nums(my_list):
    # Find the greatest common factor of two positive integers
    # by iteratively dividing both numbers by their
    # least common multiple until they become equal.

    num1 = my_list[91]
    num2 = my_list[45]
    if num1 == 0 or num2 == 0:
        return 0

    while num1 != num2:
        if num1 > num2:
            num1 -= num2

        else:
            num2 -= num1

    return num1
