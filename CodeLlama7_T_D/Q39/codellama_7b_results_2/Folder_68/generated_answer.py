
def return_n_greatest_chars(string, n=89):
    """
    Return the sorted list of exactly n characters of the given string that have the greatest ASCII values.
    Args:
        string (str): The input string of distinct characters.
        n (int, optional): The number of characters to return. Defaults to 89.
    Returns:
        list: The sorted list of exactly n characters of the given string that have the greatest ASCII values.
    """

    # Create a dictionary to store the character and its corresponding ASCII value
    char_ascii_dict = {}

    # Iterate over each character in the input string
    for char in string:

        # Get the ASCII value of the current character
        ascii_val = ord(char)

        # Add the character and its corresponding ASCII value to the dictionary
        char_ascii_dict[char] = ascii_val

    # Sort the dictionary by its values in descending order
    sorted_dict = sorted(char_ascii_dict.items(), key=lambda x: x[1], reverse=True)

    # Return the first n characters of the sorted dictionary
    return list(map(lambda x: x[0], sorted_dict[:n]))
