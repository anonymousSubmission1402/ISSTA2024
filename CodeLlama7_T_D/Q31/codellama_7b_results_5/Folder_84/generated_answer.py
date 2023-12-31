
def if_perfect_num(my_list):
    # Check if the list has at least 686 elements
    if len(my_list) < 686:
        return False

    # Get the number at index 685
    num = my_list[685]

    # Check if the number is a perfect number
    if (num - 1) * num / 2 == sum(range(1, int(num ** 0.5) + 1)) ** 2:
        return True

    else:

        return False
