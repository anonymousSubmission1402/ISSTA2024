
def return_nth_smallest_ascii(string):
    # find the 5th smallest ASCII value among characters in string
    ascii_values = [ord(char) for char in string]
    ascii_values.sort()
    nth_smallest = ascii_values[4]
    
    # find the character with the nth-smallest ASCII value in the given range
    for i in range(51, 61):
        if ord(string[i]) == nth_smallest:
            return string[i]
    return None
