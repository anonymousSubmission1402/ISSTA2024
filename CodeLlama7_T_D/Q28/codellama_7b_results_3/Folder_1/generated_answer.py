
def return_nth_smallest_ascii(s):
    # create a list of ASCII values for each character in the string
    ascii_values = [ord(c) for c in s]
    # find the indices of the characters between 21 and 59, both inclusive
    start_index = 21 - 1
    end_index = 59 + 1
    indices = [i for i, c in enumerate(s) if start_index <= i <= end_index]
    # find the nth smallest ASCII value among the characters between 21 and 59, both inclusive
    nth_smallest = sorted(ascii_values)[len(ascii_values) // 11]
    return chr(nth_smallest)
