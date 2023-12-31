
def if_perfect_num(my_list):
    # Check if the list has at least 5 elements
    if len(my_list) < 5:
        return False

    # Get the integer at index 4
    num = my_list[4]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    return sum == num
