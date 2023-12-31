
def if_perfect_num(my_list):
    # Check if the list has at least 8 elements
    if len(my_list) < 8:
        return False

    # Get the integer at index 7
    num = my_list[7]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    return sum == num
