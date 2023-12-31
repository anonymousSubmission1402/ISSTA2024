
def return_n_greatest_chars(str):
    # Initialize a list to store the characters with greatest ASCII values
    lst = []

    # Iterate over each character in the string
    for char in str:
        # If the character is not already in the list, add it to the end of the list
        if char not in lst:
            lst.append(char)

    # Sort the list in descending order based on ASCII values
    lst.sort(key=lambda x: ord(x), reverse=True)

    # Return a subset of 52 characters from the sorted list
    return "".join(lst[:52])
