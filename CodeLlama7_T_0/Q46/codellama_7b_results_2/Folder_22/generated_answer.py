
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 27, 85 and 51
    gcf = my_list[27]
    for i in range(27 + 1, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            break

    return gcf
