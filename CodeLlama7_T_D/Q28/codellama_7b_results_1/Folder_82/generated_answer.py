
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    freq = {}

    # Iterate over the characters in the string and update the frequency dictionary

    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    # Sort the frequency dictionary by value in descending order

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 15th smallest ASCII value among those characters in the string that occur between indices 0 to 14, both inclusive

    return sorted_freq[14][0]
