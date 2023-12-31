
def return_n_greatest_chars(string):
    char_list = list(set(string))  # create a set of distinct characters in the string
    sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)  # sort the list in descending order by ASCII value
    return sorted_list[:12]  # return the first 12 characters of the sorted list
