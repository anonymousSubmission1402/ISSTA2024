
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character
    char_freq = {}

    # Iterate over the characters in the string
    for char in string:

        # If the character is already in the dictionary, increment its frequency
        if char in char_freq:
            char_freq[char] += 1

        # Otherwise, add it to the dictionary with an initial frequency of 1
        else:
            char_freq[char] = 1

    # Sort the characters by their frequency in descending order
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 18th smallest ASCII value among those characters that occur between indices 17 to 34, both inclusive
    return sorted_chars[17][0]
