
def return_n_greatest_chars(my_string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # Return the first 76 characters of the sorted string
    return "".join(sorted_string[:76])
