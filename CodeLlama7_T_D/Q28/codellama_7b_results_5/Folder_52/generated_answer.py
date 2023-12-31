
def return_nth_smallest_ascii(s):
    # Find the indices of the characters in the string that occur between 46 and 72, both inclusive
    start_index = s.find('A', 46)
    end_index = s.rfind('Z', 46, 72)
    # If no character occurs between 46 and 72, return -1
    if start_index == -1 or end_index == -1:
        return -1

    # Sort the characters in the string that occur between 46 and 72 by their ASCII values
    sorted_chars = sorted(s[start_index:end_index+1], key=ord)
    # Return the 15th smallest ASCII value among the sorted characters
    return sorted_chars[14]
