
def if_perfect_num(my_list):
    # Check if the list is empty or has fewer than 60 elements
    if len(my_list) < 60:
        return False

    # Get the integer at index 59
    perfect_number = my_list[59]

    # Check if the integer is a perfect number
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            return True

    # If the loop completes without returning True, then the integer is not a perfect number
    return False
