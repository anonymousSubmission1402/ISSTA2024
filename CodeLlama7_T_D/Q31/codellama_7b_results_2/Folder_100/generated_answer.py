
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the integer at index 99 is a perfect number
    if my_list[99] in [x for x in range(1, 10000) if sum(range(1, x)) == x]:
        return True

    else:

        return False
