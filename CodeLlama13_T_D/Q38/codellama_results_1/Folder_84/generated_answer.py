
def find_subset_of_length_n(my_set):
    return sum(1 << i for i in range(len(my_set)))
