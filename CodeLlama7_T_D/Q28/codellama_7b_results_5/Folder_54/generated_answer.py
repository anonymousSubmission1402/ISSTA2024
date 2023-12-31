
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the counts of each character in the string
    char_counts = {}
    # Iterate over the characters in the string and update the count for each character
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    # Initialize a list to store the characters with their counts in descending order
    chars_with_counts = []
    # Iterate over the dictionary of character counts and add each character with its count to the list
    for char, count in char_counts.items():
        chars_with_counts.append((char, count)))
    # Sort the list of characters with their counts in descending order based on the count
    chars_with_counts.sort(key=lambda x: x[1], reverse=True)
    # Return the character with the 17th smallest ASCII value among those characters in the string that occur between indices 12 to 87, both inclusive
    return chars_with_counts[16][0]
