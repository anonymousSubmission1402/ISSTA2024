
def find_subset_of_length_n(set):
    num_subsets = 0
    for i in range(len(set)):
        for j in range(i+1, len(set)):
            if len({*set[i], *set[j]}) == 25:
                num_subsets += 1

    return num_subsets
