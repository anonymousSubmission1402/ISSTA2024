
def return_nth_smallest_ascii(s):
    # extract the characters between indices 5 and 10, both inclusive
    chars = s[5:11]
    # get a list of ASCII values for each character in the substring
    ascii_values = [ord(c) for c in chars]
    # sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # return the 6th smallest ASCII value
    return chr(sorted_ascii_values[5])
