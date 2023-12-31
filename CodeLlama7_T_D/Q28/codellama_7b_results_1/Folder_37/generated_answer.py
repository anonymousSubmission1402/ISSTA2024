
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    char_freq = {}

    # Iterate over the characters in the string and update the frequency of each character in the dictionary

    for char in string:
        if char in char_freq:
            char_freq[char] += 1

        else:
            char_freq[char] = 1

    # Sort the dictionary by value (frequency) and return the character with the 15th smallest ASCII value

    sorted_char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    nth_smallest_ascii = sorted_char_freq[14][0]

    return nth_smallest_ascii
