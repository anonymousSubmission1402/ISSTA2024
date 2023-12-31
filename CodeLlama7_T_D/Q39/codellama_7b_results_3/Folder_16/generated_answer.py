
def return_n_greatest_chars(string, n):
    """
    Return the sorted list of exactly n characters of the given string that have the greatest ASCII values.
    Args:
        string (str): The input string.
        n (int): The number of characters to return.
    Returns:
        list: The sorted list of n characters with the greatest ASCII values.
    """

    # Create a dictionary with the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    # Sort the dictionary by value in descending order
    sorted_dict = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Return the top n characters with the greatest ASCII values
    return [char for char, _ in sorted_dict[:n]]
