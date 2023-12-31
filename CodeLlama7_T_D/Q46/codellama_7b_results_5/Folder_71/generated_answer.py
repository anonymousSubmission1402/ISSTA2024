
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 24, 45 and 38
    i = 24
    j = 45
    k = 38
    while i != 1 or j != 1 or k != 1:
        if i % j == 0 and i % k == 0:
            gcf = i
            break

        elif j % i == 0 and j % k == 0:
            gcf = j
            break

        elif k % i == 0 and k % j == 0:
            gcf = k
            break

        else:

            i += 1

            if i == len(my_list):
                i = 24

    return gcf
