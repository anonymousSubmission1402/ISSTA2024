
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[63:77]]
    nth_smallest = sorted(ascii_values)[14]
    return chr(nth_smallest)
