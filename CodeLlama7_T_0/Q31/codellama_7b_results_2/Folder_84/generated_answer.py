
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 685 elements
    if len(my_list) < 685:
        return False

    # Get the element at index 685
    num = my_list[685]

    # Check if the number is a perfect number

    def is_perfect_num(n):
        sum = 0

        for i in range(1, n):
            if n % i == 0:
                sum += i

        return sum == n - 1


    return is_perfect_num(num)
