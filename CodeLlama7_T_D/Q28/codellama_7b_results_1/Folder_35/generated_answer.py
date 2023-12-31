
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Create a dictionary to store the ASCII values and their indices

    ascii_dict = {}

    # Iterate over the characters in the string

    for i, char in enumerate(char_list):
        # If the character is not already in the dictionary

        if char not in ascii_dict:
            # Add it to the dictionary with its index

            ascii_dict[char] = [i]
        else:
            # If the character is already in the dictionary, add its new index to the list of indices

            ascii_dict[char].append(i)
    # Sort the dictionary by key (ASCII value)

    sorted_ascii_dict = dict(sorted(ascii_dict.items(), key=lambda x: ord(x[0]))))
    # Get the nth smallest ASCII value and its corresponding index

    nth_smallest_ascii = list(sorted_ascii_dict.values())[50]
    return char_list[nth_smallest_ascii[0]]
