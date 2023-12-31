 def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    char_freq = {}
    # Iterate through the characters in the string
    for char in string:
        # If the character is already in the dictionary, increment its frequency
        if char in char_freq:
            char_freq[char] += 1
        # Otherwise, add the character to the dictionary with an initial frequency of 1
        else:
            char_freq[char] = 1
    # Sort the dictionary by value (frequency) in descending order
    sorted_dict = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    # Return the character with the 7th smallest ASCII value among those characters in the string that occur between indices 0 to 6, both inclusive
    return sorted_dict[6][0]
