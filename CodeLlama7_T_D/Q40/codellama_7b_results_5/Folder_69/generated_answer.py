
def return_n_smallest_chars(string):
    # Sort the string in descending order based on ASCII value
    sorted_string = sorted(string, key=lambda x: ord(x), reverse=True)
    # Create a list of exactly 65 characters from the sorted string
    smallest_characters = sorted_string[:65]
    return smallest_characters
