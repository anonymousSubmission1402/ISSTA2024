
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the index at which the number is stored (in this case, index 72) exists in the list
    if len(my_list) < 72:
        return False

    # Check if the number at index 72 is a perfect number
    if my_list[72] == sum(range(1, my_list[72])):
        return True

    else:

        return False
