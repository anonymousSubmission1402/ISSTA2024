
def return_n_greatest_chars(string):
    # create a list of tuples, where each tuple contains a character and its ASCII value
    chars = [(char, ord(char)) for char in string if char not in " "]

    # sort the list by ASCII value in descending order (largest to smallest)
    chars.sort(key=lambda x: -x[1])

    # return a list of exactly 20 characters with the greatest ASCII values, sorted in ascending order
    return [char for char, _ in chars[:20]]
