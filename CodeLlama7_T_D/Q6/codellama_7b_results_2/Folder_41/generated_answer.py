
def all_neg_ints_exclusive(my_list):
    # create a slice of the list from index 8 to index 9, both exclusive
    neg_ints = my_list[8:9]
    # filter out any positive or zero integers
    filtered_neg_ints = [x for x in neg_ints if x < 0]
    return filtered_neg_ints
