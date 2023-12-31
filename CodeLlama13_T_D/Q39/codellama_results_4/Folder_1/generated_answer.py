
def return_n_greatest_chars(string):
    # Use a list comprehension to create a list of (ASCII value, character) tuples
    chars = [(ord(c), c) for c in string if c not in '0123456789']

    # Sort the list in descending order based on the ASCII values
    sorted_chars = sorted(chars, reverse=True)

    # Create a new list of exactly 11 characters with the greatest ASCII values
    n_greatest_chars = [c for c in sorted_chars[:11]]

    return n_greatest_chars
