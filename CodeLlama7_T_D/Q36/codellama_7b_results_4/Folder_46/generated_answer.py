
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in s:

        # If the current character is greater than '<' and smaller than 'C', skip it
        if char > '<' and char < 'C':
            continue


        # Otherwise, add the current character to the list of filtered characters
        filtered_chars.append(char)

    # Join the filtered characters into a string and return it
    return "".join(filtered_chars)
