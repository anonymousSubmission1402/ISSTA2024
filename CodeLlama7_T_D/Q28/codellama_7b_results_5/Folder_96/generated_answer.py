
def return_nth_smallest_ascii(string):
    char_set = set(string)
    ascii_values = []
    for char in char_set:
        ascii_values.append(ord(char))
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii_value = sorted_ascii_values[17]
    return chr(nth_smallest_ascii_value)
