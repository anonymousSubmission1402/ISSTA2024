
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by frequency and ASCII value
    sorted_chars = sorted(char_freq.items(), key=lambda x: (x[1], ord(x[0]))))
    # Return the nth smallest ASCII value among the characters in the string that occur between indices 34 to 85, both inclusive
    return sorted_chars[20][0]
