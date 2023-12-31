
def return_n_greatest_chars(input_string):
    # sort the input string in descending order based on ASCII value
    sorted_list = sorted(input_string, key=ord, reverse=True)
    # create a list of exactly 70 characters from the sorted list
    n_greatest_chars = sorted_list[:70]
    return n_greatest_chars
