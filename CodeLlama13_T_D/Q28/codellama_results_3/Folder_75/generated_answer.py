
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(62, 83+1):
        char = string[i]
        if char not in ascii_values:
            ascii_values.append(ord(char))
    return chr(sorted(ascii_values)[9-1])
