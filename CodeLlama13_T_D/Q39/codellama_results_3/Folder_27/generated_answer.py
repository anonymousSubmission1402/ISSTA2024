
def return_n_greatest_chars(string):
    sorted_list = sorted(string, key=ord)
    return sorted_list[-82:]
