
def all_odd_ints_inclusive(my_list):
        start_index = 66
        end_index = 93
        odd_ints = []
        for i in range(start_index, end_index + 1):
            if my_list[i] % 2 != 0:
                odd_ints.append(my_list[i])
        return odd_ints
