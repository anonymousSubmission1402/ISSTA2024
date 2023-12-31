
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the number at index 51
    num = my_list[51]

    # Check if the number is a perfect number
    if num > 0 and sum(range(1, num)) == num**2 - 1:
        return True

    else:

        return False
