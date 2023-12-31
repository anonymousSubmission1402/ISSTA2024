
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the character frequencies
    freq = {}

    # Iterate through the string and update the frequency dictionary
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Find the character with the 19th smallest ASCII value
    ascii_values = []
    for char, freq in freq.items():
        ascii_value = ord(char)
        ascii_values.append((ascii_value, freq)))

    sorted_ascii_values = sorted(ascii_values, key=lambda x: (x[0], -x[1])))
    nth_smallest_ascii_value = sorted_ascii_values[19][0])
    return chr(nth_smallest_ascii_value)
