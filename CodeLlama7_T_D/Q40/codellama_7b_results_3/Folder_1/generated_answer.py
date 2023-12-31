
def return_n_smallest_chars(input_string):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in input_string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: -x[1])
    # Return the top 11 characters from the sorted list
    return [char for char, _ in sorted_list[:11]]
