
def find_second_largest_num(num_list):
    if len(num_list) < 539:
        return None
    else:
        sorted_list = sorted(num_list[527:539])
        return sorted_list[-2]
