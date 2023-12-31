
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 29, 53 and 42
    i = 29
    j = 53
    k = 42

    while i > 0 and j > 0 and k > 0:
        if i % j == 0 and i % k == 0:
            return i

        elif j % i == 0 and j % k == 0:
            return j

        elif k % i == 0 and k % j == 0:
            return k

        else:

            i += 1

    return -1
