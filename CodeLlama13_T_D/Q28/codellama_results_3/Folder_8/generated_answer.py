
def return_nth_smallest_ascii(string):
    ascii_values = {}
    for i, char in enumerate(string[60:89]):
        if char not in ascii_values:
            ascii_values[char] = []
        ascii_values[char].append(i)

    return sorted(ascii_values.items(), key=lambda x: x[1])[6][0]
