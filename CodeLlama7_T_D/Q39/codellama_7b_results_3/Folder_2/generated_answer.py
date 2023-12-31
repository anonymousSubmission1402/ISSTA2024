
def return_n_greatest_chars(my_string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # Take the top 48 characters from the sorted list
    top_48_chars = sorted_string[:48]
    return top_48_chars
